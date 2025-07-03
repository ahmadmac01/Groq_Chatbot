# 🧠 Groq Chatbot with LLaMA 3.3 70B

This is a simple chatbot built using **Streamlit** and **Groq's Python SDK**. It leverages the powerful **LLaMA 3.3 70B Versatile** model to generate intelligent and contextual responses. It features chat history, session memory, and `.env`-based API key handling.

## 🚀 Features

- 💬 Interactive chat interface using Streamlit
- 🤖 Powered by `llama-3.3-70b-versatile` via Groq API
- 🧠 Maintains session chat history (up to 15 messages)
- 🔐 Secure API key loading via `.env` file

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ahmadmac01/groq-chatbot.git
cd groq-chatbot
```
### 2. Create a .env File
Create a .env file in the root directory and add your Groq API key:
```
groq_api=your_groq_api_key_here
```
### 3. Install Requirements
Make sure you have Python 3.8+ installed.
```
pip install -r requirements.txt
```
### 4. Run the App
```
streamlit run app.py
```
### 📚 About the Model
This chatbot uses the llama-3.3-70b-versatile model from Groq, which is optimized for low-latency responses and high-quality output. It's suitable for general-purpose conversational AI tasks.

### 🧑‍💻 Author
Muhammad Ahmad

Feel free to connect or contribute!
