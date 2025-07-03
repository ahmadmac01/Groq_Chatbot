import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv  
# Load environment variables from .env file
load_dotenv()    


GROQ_API_KEY = os.getenv("groq_api")
MODEL_NAME =  "llama-3.3-70b-versatile"
MAX_HISTORY = 15

client = Groq(api_key=GROQ_API_KEY)

# === Session State for History ===
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": "You are a helpful assistant. Answer questions to the best of your abilities. Be concise and informative."}
    ]

# === Title and Chat Input ===
st.title("Groq Chatbot")
user_input = st.chat_input("Type your message here...")

# === Handle User Message ===
if user_input:
    # Add user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Keep last N messages in history
    if len(st.session_state.chat_history) > MAX_HISTORY + 1:
        st.session_state.chat_history = [st.session_state.chat_history[0]] + st.session_state.chat_history[-MAX_HISTORY:]


    try:
        response = client.chat.completions.create(
            messages=st.session_state.chat_history,
            model=MODEL_NAME,
            max_completion_tokens=264,
        )
        reply = response.choices[0].message.content.strip()


        st.session_state.chat_history.append({"role": "assistant", "content": reply})
    except Exception as e:
        reply = f"⚠️ Error: {e}"
        st.session_state.chat_history.append({"role": "assistant", "content": reply})

# === Display Chat History ===
for msg in st.session_state.chat_history[1:]: 
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
