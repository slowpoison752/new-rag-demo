import os
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from get_embedding_function import get_embedding_function
from config import config

CHROMA_PATH = config.CHROMA_PATH

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

class RAGService:
    def __init__(self):
        self.embedding_function = get_embedding_function()
        self.db = Chroma(persist_directory=CHROMA_PATH, embedding_function=self.embedding_function)
        self.model = Ollama(
            model=config.LLM_MODEL,
            base_url=config.OLLAMA_BASE_URL
        )
        self.prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    
    def query(self, question: str) -> dict:
        """
        Query the RAG system with a question and return structured response
        """
        try:
            # Search the DB
            results = self.db.similarity_search_with_score(question, k=5)
            
            # Prepare context
            context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
            
            # Generate prompt
            prompt = self.prompt_template.format(context=context_text, question=question)
            
            # Get response
            response_text = self.model.invoke(prompt)
            
            # Prepare sources
            sources = [doc.metadata.get("id", None) for doc, _score in results]
            
            return {
                "answer": response_text,
                "sources": sources,
                "context": context_text[:500] + "..." if len(context_text) > 500 else context_text
            }
        except Exception as e:
            return {
                "answer": f"Error processing query: {str(e)}",
                "sources": [],
                "context": ""
            }

# Global RAG service instance
rag_service = RAGService() 