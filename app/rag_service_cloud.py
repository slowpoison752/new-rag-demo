import os
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from config import config

CHROMA_PATH = config.CHROMA_PATH

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

class RAGServiceCloud:
    def __init__(self):
        # Use OpenAI embeddings instead of Ollama
        self.embedding_function = OpenAIEmbeddings(
            openai_api_key=config.OPENAI_API_KEY,
            model="text-embedding-ada-002"
        )
        self.db = Chroma(persist_directory=CHROMA_PATH, embedding_function=self.embedding_function)
        
        # Use OpenAI Chat instead of Ollama
        self.model = ChatOpenAI(
            openai_api_key=config.OPENAI_API_KEY,
            model_name="gpt-3.5-turbo",
            temperature=0.1
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
            response = self.model.invoke(prompt)
            response_text = response.content
            
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
rag_service_cloud = RAGServiceCloud() 