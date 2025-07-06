# 🚀 RAG Demo - Deployment Guide

## 🎯 Overview

This RAG (Retrieval-Augmented Generation) demo can be deployed to multiple platforms. Choose the option that best fits your needs:

## 🏆 **Recommended: Railway (Easiest)**

### **Why Railway?**
- ✅ **No CLI required** - Everything through web interface
- ✅ **5-minute setup** 
- ✅ **$5 free credit** monthly
- ✅ **Auto-deploy** from GitHub
- ✅ **Super easy** to use

### **Railway Deployment Steps:**

1. **Sign up** at [railway.app](https://railway.app)
2. **Connect your GitHub repository**
3. **Set environment variables:**
   ```
   OPENAI_API_KEY=your-openai-api-key-here
   CHROMA_PATH=chroma
   DATA_PATH=data
   EMBEDDING_MODEL=text-embedding-ada-002
   LLM_MODEL=gpt-3.5-turbo
   ```
4. **Deploy!** (takes 2-3 minutes)

---

## 🎯 **Alternative: Fly.io (Cost Optimized)**

### **Why Fly.io?**
- ✅ **Free tier**: 3 shared-cpu-1x 256mb VMs
- ✅ **Auto-scaling to zero** when idle
- ✅ **Global edge network** for fast performance
- ✅ **Pay-per-use** pricing

### **Fly.io Deployment Steps:**

1. **Install Fly CLI:**
   ```bash
   # Download from: https://github.com/superfly/flyctl/releases
   # Extract to C:\flyctl and add to PATH
   ```

2. **Sign up** at [fly.io](https://fly.io)

3. **Deploy:**
   ```bash
   fly auth login
   fly launch
   fly deploy
   fly secrets set OPENAI_API_KEY="your-key"
   ```

---

## 🎯 **Alternative: Render (Also Easy)**

### **Why Render?**
- ✅ **750 free hours** monthly
- ✅ **Web interface** deployment
- ✅ **Auto-deploy** from GitHub
- ✅ **Good documentation**

### **Render Deployment Steps:**

1. **Sign up** at [render.com](https://render.com)
2. **Connect your GitHub repository**
3. **Create new Web Service**
4. **Set environment variables** in dashboard
5. **Deploy!**

---

## 🔧 **Local Development**

### **Prerequisites:**
- Python 3.11+
- Docker Desktop
- OpenAI API key

### **Quick Start:**
```bash
# Clone the repository
git clone <your-repo-url>
cd rag-demo

# Set up environment
python setup_env.py

# Run with Docker
docker-compose up -d

# Test the API
curl http://localhost:8000/health
```

---

## 📁 **Project Structure**

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
└── DEPLOYMENT.md          # This guide
```

---

## 🚨 **Important Notes**

### **Environment Variables:**
- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `CHROMA_PATH`: Vector database path (default: chroma)
- `DATA_PATH`: Data files path (default: data)

### **Before Deploying:**
1. **Get your OpenAI API key** from [platform.openai.com](https://platform.openai.com/api-keys)
2. **Test locally first** with Docker
3. **Choose your deployment platform** based on needs

### **Cost Optimization:**
- **Railway**: $5 free credit monthly
- **Fly.io**: 3 free VMs, auto-scales to zero
- **Render**: 750 free hours monthly

---

## 🎉 **Quick Comparison**

| Platform | Setup Time | Free Tier | CLI Required | Ease of Use |
|----------|------------|-----------|--------------|-------------|
| **Railway** | 5 min | $5 credit | ❌ | 🏆 **Easiest** |
| **Fly.io** | 15 min | 3 VMs | ✅ | Medium |
| **Render** | 10 min | 750 hours | ❌ | Easy |

**Recommendation: Start with Railway for the easiest deployment experience!** 