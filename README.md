# 🕵️ LangChain - Chat with Search Agents

This project is a **Streamlit-based AI chatbot** that integrates **LangChain**, **Groq API**, and multiple search tools (Wikipedia, Arxiv, and DuckDuckGo).  
It allows users to ask questions and get intelligent answers with real-time search capabilities.

---

## 🚀 Features
- **Chat Interface** built using Streamlit.
- **Groq API Integration** for running LLMs.
- **Wikipedia Search** integration.
- **Arxiv Paper Search** for academic research.
- **DuckDuckGo Web Search** for general queries.
- **Agent-based Reasoning** using LangChain tools.

---

## 🛠️ Tech Stack
- [Python](https://www.python.org/)  
- [Streamlit](https://streamlit.io/)  
- [LangChain](https://www.langchain.com/)  
- [Groq API](https://console.groq.com/)  
- [Wikipedia API](https://pypi.org/project/wikipedia/)  
- [Arxiv API](https://pypi.org/project/arxiv/)  
- [DuckDuckGo Search](https://pypi.org/project/duckduckgo-search/)  

---


## 🔑 Environment Variables
Create a `.env` file in the root directory and add the following:
```env
GROQ_API_KEY=your_groq_api_key_here
```

## Installation
### 1. Clone Repo
```env
git clone https://github.com/your-username/langchain-search-agents.git
cd langchain-search-agents
```

### 2. Create a virtual environment
```env
python -m venv venv
source venv/bin/activate
```

### 4. Install dependencies
```env
pip install -r requirements.txt
```

## ▶️ Usage
Run the Streamlit app:
``` env
streamlit run app.py
```
Open your browser at 
```
https://aisearchagent-9unscezqjpzbphwz3xg5kq.streamlit.app/
```
to use the chatbot.

## 🧪 How it Works
The user inputs a query in the chat.

The app uses LangChain Agents to decide which tool to use:

- Wikipedia for general knowledge.
- Arxiv for research papers.
- DuckDuckGo for web search.

The response is generated and streamed in real-time using the Groq LLM.
The chat history is maintained in st.session_state

### 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### 📜 License
This project is licensed under the MIT License.
