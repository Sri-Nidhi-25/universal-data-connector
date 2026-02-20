# 🚀 Universal Data Connector API

An AI-powered backend system that integrates multiple data sources (CRM, Support, Analytics), applies intelligent summarization, and enables conversational insights using Groq LLM. Built for voice-optimized interactions with structured, voice-friendly response formats.

## 📌 Project Overview

Universal Data Connector is a production-ready FastAPI application that:

- ✨ Connects to multiple structured data sources (CRM, Support, Analytics)
- 🎯 Applies business rules and response optimization for voice conversations
- 📊 Generates intelligent summaries automatically
- 🤖 Provides AI-powered chat interaction through Groq LLM
- 📈 Returns structured metadata with every response
- 🔍 Automatically identifies and adapts to different data types (tabular, time-series, hierarchical)
- 📱 Optimizes responses for low-latency voice contexts

The system is designed with clean architecture principles and is easily extendable to new data sources or AI providers.

## 🏗 Architecture Overview

```
          ┌─────────────────────────────────────┐
          │         FastAPI Application         │
          └─────────────────────────────────────┘
                              │
            ┌─────────┼──────────┬─────────────┐
            │         │          │             │
            ▼         ▼          ▼             ▼
         Routers   Services   Connectors      LLM
         (health,  (business,  (CRM,         (Groq)
          data,    optimizer)  Support,        │ 
          chat)       │         Analytics)     │
            │         │         │              │
            └─────────┼─────────┼──────────────┘
                      │         │
                      ▼         ▼
                    JSON   Groq API
               Data Files       │
                      ┼─────────┼
                           │
                           ▼
                 ┌───────────────────────┐
                 │ Structured Response:  │
                 │ -  Data               │
                 │ -  Summary            │
                 │ -  Metadata           │
                 │ -  Data Type Info     │
                 └───────────────────────┘
```

## ⚙️ Tech Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **Pydantic** - Data validation using Python type annotations
- **Groq LLM** - Fast, cost-efficient LLM for AI responses
- **Uvicorn** - Lightning-fast ASGI server
- **Python 3.10+** - Modern Python with type hints
- **Docker & Docker Compose** - Containerized deployment

## 🧩 Key Features Implemented

✅ **Modular Architecture** - Clean separation of concerns
✅ **Multiple Data Connectors** - CRM, Support, Analytics support
✅ **Business Rule Enforcement** - Limit handling, prioritization
✅ **Smart Summarization Engine** - Aggregate metrics for voice contexts
✅ **Data Type Identification** - Automatic detection and handling
✅ **Metadata Generation** - Context awareness for LLM integration
✅ **AI Integration (Groq)** - Seamless LLM-powered chat
✅ **Logging & Error Handling** - Production-ready error management
✅ **Swagger Documentation** - Auto-generated API docs
✅ **Environment Configuration** - Secure config management

## ▶️ How To Run

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Add Environment Variables

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_api_key_here
```

You can get your Groq API key from [Groq's console](https://console.groq.com).

### 3️⃣ Start Server

```bash
uvicorn app.main:app --reload
```

### 4️⃣ Open Swagger UI

Navigate to `http://127.0.0.1:8000/docs` to explore the API interactively.

### Docker Setup (Alternative)

```bash
docker-compose up --build
```

Visit `http://localhost:8000/docs` after the container starts.

## 📡 API Endpoints

### Health Check

**GET** `/health`

Returns the health status of the application.

**Response:**
```json
{
  "status": "ok"
}
```

### Data Retrieval

**GET** `/data/{source}`

Fetch data from a specific source with optional filtering and optimization.

**Parameters:**
- `source` (path) - Data source: `crm`, `support`, or `analytics`
- `limit` (query) - Maximum number of records (default: 10, for voice optimization)
- `optimize` (query) - Enable summarization (default: true)

**Sample Response:**
```json
{
  "data_type": "tabular_crm",
  "summary": {
    "total_customers": 50,
    "active": 40,
    "inactive": 10
  },
  "data": [
    {
      "id": 1,
      "name": "Acme Corp",
      "status": "active",
      "created_at": "2026-01-15"
    }
  ],
  "metadata": {
    "total_results": 50,
    "returned_results": 10,
    "data_freshness": "Data as of 2026-02-20T10:22:31",
    "has_more": true
  }
}
```

### AI Chat

**POST** `/chat`

Get AI-powered insights using Groq LLM.

**Request Body:**
```json
{
  "message": "Summarize CRM performance"
}
```

**Response:**
```json
{
  "model_response": "CRM shows strong active customer engagement with minimal inactive accounts. Out of 50 customers, 40 are active (80%). This indicates healthy customer retention and engagement levels."
}
```

## 🧠 AI Provider: Groq

This project uses **Groq API** for fast, intelligent responses:

- **Model**: `llama-3.1-8b-instant`
- **Latency**: Ultra-low latency perfect for voice interactions
- **Cost**: Highly cost-efficient inference
- **Compatibility**: OpenAI-compatible interface
- **Use Case**: Real-time conversational AI for voice applications

## 🎯 Voice-Optimized Business Rules

The system implements intelligent voice-specific optimizations:

- **Limit results** - Default max 10 items for clear voice responses
- **Prioritization** - Returns most recent/relevant data first
- **Summarization** - Aggregates metrics instead of raw data when appropriate
- **Context awareness** - Includes helpful metadata (e.g., "showing 3 of 47 results")
- **Freshness indicators** - Shows data currency (e.g., "Data as of 2 hours ago")
- **Smart filtering** - Automatically filters based on business context

## 📁 Project Structure

```
D:\UNIVERSAL-DATA-CONNECTOR\UNIVERSAL-DATA-CONNECTOR
│   .DS_Store
│   .env.example
│   .gitignore
│   docker-compose.yml
│   Dockerfile
│   README.md
│   README_new.md
│   requirements.txt
│
├───.benchmarks
├───.pytest_cache
│   │   .gitignore
│   │   CACHEDIR.TAG
│   │   README.md
│   │
│   └───v
│       └───cache
│               lastfailed
│               nodeids
│
├───app
│   │   .DS_Store
│   │   config.py
│   │   main.py
│   │
│   ├───connectors
│   │   │   analytics_connector.py
│   │   │   base.py
│   │   │   crm_connector.py
│   │   │   support_connector.py
│   │   │
│   │   └───__pycache__
│   │           analytics_connector.cpython-313.pyc
│   │           base.cpython-313.pyc
│   │           crm_connector.cpython-313.pyc
│   │           support_connector.cpython-313.pyc
│   │
│   ├───models
│   │   │   common.py
│   │   │
│   │   └───__pycache__
│   │           common.cpython-313.pyc
│   │
│   ├───routers
│   │   │   chat.py
│   │   │   data.py
│   │   │   health.py
│   │   │
│   │   └───__pycache__
│   │           chat.cpython-313.pyc
│   │           data.cpython-313.pyc
│   │           health.cpython-313.pyc
│   │
│   ├───services
│   │   │   business_rules.py
│   │   │   data_identifier.py
│   │   │   llm_service.py
│   │   │   voice_optimizer.py
│   │   │
│   │   └───__pycache__
│   │           business_rules.cpython-313.pyc
│   │           data_identifier.cpython-313.pyc
│   │           llm_service.cpython-313.pyc
│   │           voice_optimizer.cpython-313.pyc
│   │
│   ├───utils
│   │   │   logging.py
│   │   │
│   │   └───__pycache__
│   │           logging.cpython-313.pyc
│   │
│   └───__pycache__
│           config.cpython-313.pyc
│           main.cpython-313.pyc
│
├───data
│       analytics.json
│       customers.json
│       support_tickets.json
│
└───tests
    │   test_api.py
    │   test_business_rules.py
    │   test_connectors.py
    │
    └───__pycache__
            test_api.cpython-313-pytest-8.4.2.pyc
            test_business_rules.cpython-313-pytest-8.4.2.pyc
            test_connectors.cpython-313-pytest-8.4.2.pyc
```

## 🔮 Future Improvements

- 🔐 Add authentication & role-based access control
- ⏱️ Add rate limiting per data source
- 💾 Add caching layer (Redis) for frequently accessed data
- 🗄️ Add relational database support (PostgreSQL/MySQL)
- 📊 Add data export functionality (CSV, Excel)
- 🔄 Add real-time data updates via WebSocket
- 📱 Add web UI dashboard
- 🧪 Expand test coverage (unit, integration, E2E)
- 🚀 Add CI/CD pipeline (GitHub Actions)
- 🌐 Multi-language support for voice responses

## 🚀 Getting Started - Step by Step

### For Local Development:

1. Clone the repository
   ```bash
   git clone https://github.com/Sri-Nidhi-25/universal-data-connector.git
   cd universal-data-connector
   ```

2. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables
   ```bash
   cp .env.example .env
   # Edit .env and add your GROQ_API_KEY
   ```

5. Run the application
   ```bash
   uvicorn app.main:app --reload
   ```

6. Access the API
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

### For Docker:

```bash
docker-compose up --build
```

The API will be available at `http://localhost:8000`.

## 🧪 Testing

Run the test suite:

```bash
pytest tests/ -v
```

Run with coverage:

```bash
pytest tests/ --cov=app --cov-report=html
```

## 📝 API Examples

### Example 1: Get CRM Data

```bash
curl -X GET "http://localhost:8000/data/crm?limit=5&optimize=true"
```

### Example 2: Get Unoptimized Support Data

```bash
curl -X GET "http://localhost:8000/data/support?limit=10&optimize=false"
```

### Example 3: Chat with AI

```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "What is our customer satisfaction trend?"}'
```

## 🎓 Learning Outcomes

By working with this project, you'll learn:

1. **API Design** - Building clean, RESTful APIs with FastAPI
2. **Type Safety** - Using Pydantic models and Python type hints
3. **Abstraction** - Creating reusable base classes and interfaces
4. **Business Logic** - Implementing smart filtering and optimization rules
5. **LLM Integration** - Understanding function calling and AI integration patterns
6. **Production Readiness** - Logging, error handling, configuration management
7. **Voice UX** - Optimizing responses for conversational AI and voice interactions
8. **Containerization** - Docker and container orchestration basics

## 📊 Project Status

**Status**: MVP → Production-Ready Backend

This project demonstrates a production-quality backend system with:
- ✅ Solid architectural foundations
- ✅ Real-world data handling
- ✅ LLM integration
- ✅ Voice-optimized responses
- ✅ Comprehensive documentation



