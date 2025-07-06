#!/usr/bin/env python3
"""
Setup script to help configure environment variables for the RAG project.
"""

import os
from pathlib import Path

def create_env_file():
    """Create a .env file with template values"""
    env_content = """# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_BASE_URL=https://api.openai.com/v1

# Ollama Configuration (for local development)
OLLAMA_BASE_URL=http://localhost:11434

# Azure Configuration (for deployment)
AZURE_SEARCH_ENDPOINT=your_azure_search_endpoint
AZURE_SEARCH_KEY=your_azure_search_key
AZURE_SEARCH_INDEX=your_azure_search_index

# Application Configuration
CHROMA_PATH=chroma
DATA_PATH=data

# Model Configuration
EMBEDDING_MODEL=nomic-embed-text
LLM_MODEL=phi3:mini
"""
    
    env_file = Path(".env")
    if env_file.exists():
        print(".env file already exists. Skipping creation.")
        return
    
    with open(env_file, "w") as f:
        f.write(env_content)
    
    print("Created .env file with template values.")
    print("Please edit .env file and add your actual API keys.")

def main():
    print("Setting up environment configuration...")
    create_env_file()
    print("\nNext steps:")
    print("1. Edit the .env file and add your OpenAI API key")
    print("2. For local development, make sure Ollama is running")
    print("3. For Docker deployment, the environment is already configured")

if __name__ == "__main__":
    main() 