# 🤖 Nova AI Assistant

A responsive AI chatbot built using **Python**, **Streamlit**, **Groq API (Llama 3)**, and **MySQL**. The application provides a ChatGPT-like conversational experience with persistent chat history, user authentication, memory, and real-time streaming responses.

---

## 📌 Project Overview

Nova AI Assistant is a conversational AI application developed as part of an AI/ML technical assessment.

The chatbot supports:

- Human-like conversations
- Context-aware responses
- Persistent conversation history
- User memory across conversations
- Multiple LLM model selection
- Real-time streaming responses
- Responsive web interface

---

## 🚀 Features

### ✅ User Authentication

- Username-based login
- Automatic user creation for new users
- Secure session management

---

### ✅ ChatGPT-like Interface

- Clean and responsive UI
- Chat-style conversation layout
- Streaming AI responses
- Response time display

---

### ✅ AI Models

Supports multiple Groq-hosted Llama models.

- Llama 3.3 70B Versatile
- Llama 3.1 8B Instant

Users can switch models directly from the sidebar.

---

### ✅ Conversation Management

- Create New Chat
- View previous conversations
- Delete conversations
- Automatic conversation titles

---

### ✅ Persistent Chat History

All conversations are stored in MySQL.

When the user logs in again:

- Previous chats are loaded automatically
- Context is preserved
- Conversations remain available

---

### ✅ Memory System

The assistant remembers user information across conversations.

Example:

User:
> My name is Sudhan.

Later...

User:
> What is my name?

Assistant:
> Your name is Sudhan.

The memory is stored separately from chat history.

---

### ✅ Input Validation

The chatbot validates user input before sending requests to the AI model.

Examples:

- Empty messages
- Invalid inputs
- Error handling

---

### ✅ Streaming Responses

Responses are streamed token-by-token to provide a smoother user experience similar to ChatGPT.

---

### ✅ Error Handling

The application gracefully handles:

- API failures
- Database errors
- Invalid inputs

without crashing.

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Streamlit | Web Interface |
| Groq API | Large Language Model |
| Llama 3 | AI Model |
| MySQL | Database |
| mysql-connector-python | Database Connectivity |
| python-dotenv | Environment Variables |

---

# 📂 Project Structure

```
chatgpt_clone/
│
├── assets/
│
├── components/
│   ├── chat.py
│   ├── login.py
│   └── sidebar.py
│
├── app.py
├── auth.py
├── chatbot.py
├── database.py
├── memory.py
├── prompt.py
├── utils.py
├── requirements.txt
├── .env
└── README.md
```

---

# 🗄 Database

The project uses **MySQL**.

Tables:

- users
- conversations
- messages
- memory

These tables store:

- User accounts
- Conversation history
- Individual messages
- Long-term memory

---

# ⚙ Installation

## 1. Clone the project

```bash
cd chatgpt_clone
```

---

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Configure Environment Variables

Create a `.env` file.

Example:

```env
GROQ_API_KEY=your_groq_api_key

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=chatbot_db
```

---

## 4. Create MySQL Database

```sql
CREATE DATABASE chatbot_db;
```

Create the required tables before running the application.

---

## 5. Run the Application

```bash
streamlit run app.py
```

---

# 💬 Example Workflow

Login

↓

Create New Chat

↓

Ask Questions

↓

Streaming AI Response

↓

Conversation Saved

↓

Logout

↓

Login Again

↓

Previous Conversations Loaded Automatically

---

# 📸 Screens

- Login Screen
- Chat Interface
- Sidebar with Conversations
- Model Selection
- Streaming Responses
- Persistent Chat History

---

# 🎯 Assignment Requirements Coverage

| Requirement | Status |
|-------------|--------|
| Human-like conversation | ✅ |
| Responsive interface | ✅ |
| NLP conversation handling | ✅ |
| Context-aware responses | ✅ |
| Conversation history | ✅ |
| Performance optimization | ✅ |

---

# 📈 Future Improvements

- Markdown rendering enhancements
- Code syntax highlighting
- File upload support
- Image understanding
- Voice input/output
- Conversation search
- Conversation renaming
- Multi-user authentication
- Docker deployment
- Cloud deployment

---

# 👨‍💻 Developer

**Sudharsan M S**

AI / ML Developer

Built using:

- Python
- Streamlit
- Groq API
- Llama 3
- MySQL

---

## Thank You

Thank you for reviewing this project.

This project was developed as part of an AI/ML technical assessment to demonstrate practical skills in conversational AI, backend integration, database management, and modern Python application development.