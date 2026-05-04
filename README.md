# Valura AI — AI Microservice Assignment

## Overview

This project implements a FastAPI-based AI microservice that acts as an intelligent assistant for investors.
It processes user queries, ensures safety, classifies intent, routes to appropriate agents, and streams responses in real time using Server-Sent Events (SSE).

---

##  Features

### Safety Guard

* Runs before any LLM call
* Blocks harmful queries (insider trading, manipulation, etc.)
* No external calls (fast execution <10ms)

### Intent Classifier

* Uses LLM to classify:

  * Intent
  * Entities (tickers, amount, etc.)
  * Target agent
  * Safety metadata
* Handles follow-up queries using history

### Portfolio Health Agent

* Analyzes user portfolio
* Provides:

  * Concentration risk
  * Performance metrics
  * Benchmark comparison
  * Actionable insights
* Handles empty portfolio case
* Includes disclaimer

### Routing System

* Routes queries to appropriate agent
* Returns structured response for unimplemented agents

### Streaming API (SSE)

* Real-time response streaming
* Event-based communication:

  * status
  * classification
  * data
  * error

---

## Project Structure

```
src/
 ├── api/            # FastAPI routes
 ├── guards/         # Safety guard
 ├── classifier/     # Intent classifier
 ├── router/         # Request dispatcher
 ├── agents/         # Portfolio health agent
 ├── services/       # LLM service
 ├── models/         # Pydantic models

tests/               # Pytest test cases
```

---

## Setup Instructions

### 1. Clone repo

```
git clone <your-repo-url>
cd valura-ai-assignment
```

---

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Create `.env` file

```
OPENAI_API_KEY=your_api_key_here
```

---

### 5. Run server

```
python -m uvicorn src.main:app --reload
```

---

### 6. Open API docs

```
http://127.0.0.1:8000/docs
```

---

##  API Usage

### Streaming Endpoint

POST `/query`

Example request:

```json
{
  "query": "How is my portfolio doing?",
  "context": {
    "portfolio": [
      {"ticker": "NVDA", "value": 60000},
      {"ticker": "AAPL", "value": 20000}
    ]
  },
  "history": []
}
```

---

### Demo Endpoint (Non-streaming)

POST `/query-test`

---

## Testing

Run:

```
pytest tests/ -v
```

* LLM calls are mocked
* Ensures CI runs without API key

---

## Performance Considerations

* Safety guard <10ms (no external calls)
* Single LLM call for classification
* Lightweight streaming using SSE
* Designed to meet:

  * <2s first token latency
  * <6s full response time

---

## Safety Design

* Blocks:

  * Insider trading
  * Market manipulation
  * Guaranteed returns
* Allows educational queries

---

## Trade-offs

* In-memory session storage for simplicity
* Mocked LLM in tests instead of real API
* Basic portfolio calculations (can be extended with real market data)

---

## Future Improvements

* Add more agents (market research, strategy, etc.)
* Integrate real-time market APIs
* Add caching for repeated queries
* Improve classifier accuracy with embeddings

---

## Defence Video

(Add your video link here)

---


