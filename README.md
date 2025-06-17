# 🤖 Agentix: Smarter conversations, your way.

An intelligent, role-based AI chatbot system built using **LangGraph**, **Groq**, and **Tavily**. It enables users to define agent behavior dynamically and optionally allow web search. Comes with a modern **Streamlit** frontend and a **FastAPI** backend.

---

## 📁 Project Structure

```

.
├── backend
│   └── backend.py          # FastAPI server for chatbot API
│
├── frontend
│   └── frontend.py         # Streamlit UI for interacting with AI agents
│
├── src
│   ├── ai\_agent.py         # LangGraph agent setup, model config, Tavily tool
│   └── .env                # API keys for Groq, Tavily, etc.
|__requirements.txt

````

---

## 🚀 Features

- 🧠 **Agent Role Customization** — Define agent persona with system prompt
- ⚡ **Groq Integration** — Fast response from LLaMA 3-based models
- 🌐 **Tavily Search** — Optional web search integrated via tools
- 💬 **Interactive Chat UI** — Built using Streamlit
- 🔗 **Modular Backend** — Powered by FastAPI
- 🧩  **Pydantic** – Data validation and parsing of request payloads (Used in backend.py to strictly define and validate the structure of incoming API requests via the RequestState class.)

---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/langgraph-ai-agent.git
cd langgraph-ai-agent
````

### 2. Setup Python Environment

```bash
pip install -r requirements.txt
```

### 3. Add API Keys

Create a `.env` file in `src/`:

```
GROQ_API_KEY=your-groq-key
TAVILY_API_KEY=your-tavily-key
GOOGLE_API_KEY=your-google-key (optional)
```

### 4. Start Backend

```bash
cd backend
uvicorn backend:app --reload --port 9999
```

### 5. Run Frontend

```bash
cd ../frontend
streamlit run frontend.py
```

---

## 📝 Todo

* [ ] Add support for more providers (OpenAI, Gemini)
* [ ] Add history/chat memory
* [ ] Deploy to cloud

---

## 📄 License

MIT License

---

## 👤 Author

Made by **Vansh Dalal**

```
