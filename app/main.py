from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
from app.rag_service import rag_service

# Create FastAPI app
app = FastAPI(
    title="RAG Knowledge Base API",
    description="A RAG (Retrieval-Augmented Generation) API for querying PDF documents",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str
    sources: List[str]
    context: str

class HealthResponse(BaseModel):
    status: str
    message: str

@app.get("/", response_model=HealthResponse)
async def root():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        message="RAG Knowledge Base API is running"
    )

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        message="RAG Knowledge Base API is running"
    )

@app.post("/query", response_model=QueryResponse)
async def query_knowledge_base(request: QueryRequest):
    """
    Query the knowledge base with a question
    
    Args:
        request: QueryRequest containing the question
        
    Returns:
        QueryResponse with answer, sources, and context
    """
    try:
        if not request.question.strip():
            raise HTTPException(status_code=400, detail="Question cannot be empty")
        
        result = rag_service.query(request.question)
        return QueryResponse(**result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

@app.get("/docs")
async def get_docs():
    """Redirect to API documentation"""
    return {"message": "API documentation available at /docs"}

@app.get("/test")
async def test_endpoint():
    """Simple test endpoint that doesn't use Ollama"""
    return {
        "message": "API is working correctly",
        "rag_service_available": rag_service is not None
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 