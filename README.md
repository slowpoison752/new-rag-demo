# 🚀 RAG Demo - Retrieval-Augmented Generation System

A complete RAG (Retrieval-Augmented Generation) system built with FastAPI, Chroma vector database, and OpenAI/LangChain. This project demonstrates how to build a knowledge-based Q&A system that can answer questions based on your documents.

## 🎯 Features

- **📚 Document Processing**: Extract and embed text from PDFs
- **🔍 Semantic Search**: Find relevant documents using vector similarity
- **🤖 AI-Powered Answers**: Generate contextual responses using LLMs
- **🌐 Web API**: RESTful API for easy integration
- **🐳 Docker Support**: Containerized for easy deployment
- **☁️ Multi-Platform Deployment**: Support for Railway, Fly.io, Render, and more

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Docker Desktop
- OpenAI API key

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd rag-demo
   ```

2. **Set up environment**
   ```bash
   python setup_env.py
   # Edit .env file with your OpenAI API key
   ```

3. **Run with Docker**
   ```bash
   docker-compose up -d
   ```

4. **Test the API**
   ```bash
   curl http://localhost:8000/health
   ```

## 📁 Project Structure

```
rag-demo/
├── app/                    # FastAPI application
│   ├── main.py            # Local version (with Ollama)
│   ├── main_cloud.py      # Cloud version (with OpenAI)
│   └── rag_service.py     # RAG service implementation
├── data/                   # Sample data files
├── chroma/                 # Vector database (auto-created)
├── requirements_fastapi.txt # Local dependencies
├── requirements_cloud.txt  # Cloud dependencies
├── docker-compose.yml      # Local development
├── Dockerfile.cloud        # Cloud deployment
├── config.py              # Configuration management
└── DEPLOYMENT.md          # Deployment guide
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file with:
```env
OPENAI_API_KEY=your-openai-api-key-here
CHROMA_PATH=chroma
DATA_PATH=data
EMBEDDING_MODEL=text-embedding-ada-002
LLM_MODEL=gpt-3.5-turbo
```

### API Endpoints

- `GET /health` - Health check
- `GET /test` - Test endpoint
- `POST /query` - Query the RAG system

Example query:
```bash
curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"question": "What is this knowledge base about?"}'
```

## 🚀 Deployment

This project supports multiple deployment platforms:

### 🏆 **Recommended: Railway**
- **No CLI required** - Everything through web interface
- **5-minute setup** 
- **$5 free credit** monthly
- **Auto-deploy** from GitHub

### 🎯 **Alternative: Fly.io**
- **Free tier**: 3 shared-cpu-1x 256mb VMs
- **Auto-scaling to zero** when idle
- **Global edge network** for fast performance

### 🎯 **Alternative: Render**
- **750 free hours** monthly
- **Web interface** deployment
- **Auto-deploy** from GitHub

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

## 🛠️ Development

### Adding New Documents

1. **Place PDFs** in the `data/` directory
2. **Run the population script**:
   ```bash
   python populate_database.py
   ```
3. **Restart the API** to load new documents

### Customizing the RAG System

- **Embedding Model**: Change in `config.py`
- **LLM Model**: Modify in `app/rag_service.py`
- **Prompt Template**: Edit in `app/rag_service.py`
- **Search Parameters**: Adjust in `app/rag_service.py`

## 📊 Performance

- **Search Speed**: < 100ms for most queries
- **Response Time**: 1-3 seconds depending on LLM
- **Scalability**: Handles multiple concurrent requests
- **Memory Usage**: Optimized for cloud deployment

## 🔒 Security

- **API Keys**: Stored securely in environment variables
- **No hardcoded secrets** in the codebase
- **Input validation** on all endpoints
- **Error handling** prevents information leakage

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally with Docker
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

- **Issues**: Create an issue on GitHub
- **Documentation**: Check [DEPLOYMENT.md](DEPLOYMENT.md) for deployment help
- **Questions**: Open a discussion on GitHub

---

**Built with ❤️ using FastAPI, LangChain, and OpenAI**# Updated for cloud deployment
