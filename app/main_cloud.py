from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import os

# Import the cloud RAG service
try:
    from app.rag_service_cloud import rag_service_cloud
except ImportError:
    rag_service_cloud = None

app = FastAPI(title="RAG Knowledge Base API (Cloud)", version="1.0.0")

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str
    sources: list
    context: str

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "message": "RAG Knowledge Base API (Cloud) is running"
    }

@app.get("/test")
async def test_endpoint():
    """Simple test endpoint"""
    return {
        "message": "Cloud API is working correctly",
        "rag_service_available": rag_service_cloud is not None
    }

@app.post("/query", response_model=QueryResponse)
async def query_rag(request: QueryRequest):
    """Query the RAG system"""
    if not rag_service_cloud:
        raise HTTPException(status_code=500, detail="RAG service not available")
    
    try:
        result = rag_service_cloud.query(request.question)
        return QueryResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 