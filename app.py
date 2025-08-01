import streamlit as st
from langchain_groq import ChatGroq
import os
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler

from dotenv import load_dotenv
load_dotenv()
#groq_api_key = os.getenv("GROQ_API_KEY")
#groq_api_key = st.secrets["GROQ_API_KEY"]
#sidebar settings
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

wikipedia_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wikipedia = WikipediaQueryRun(api_wrapper=wikipedia_wrapper)

search = DuckDuckGoSearchRun(name="Search")

st.title("LangChain - Chat with Search Agents")

#
st.sidebar.title("Settings")
groq_api_key = st.sidebar.text_input("Enter your Groq API key", type="password")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistent", "content": "Hi, I'am a chabot who can search the web. How can I help you today?"},   
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


if  prompt := st.chat_input(placeholder="What is Machine Learning?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    
    llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192", streaming=True)

    tools = [arxiv, wikipedia, search]
    search_agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True,
        verbose = False)
    
    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({'role' : 'assistant', 'content' : response})
        st.write(response)
