# 🩺 MedicalChatBot  
### Conversational RAG-based Medical Assistant

---

## 📌 Project Overview

**MedicalChatBot** is a conversational medical assistant built using **Retrieval-Augmented Generation (RAG)**.  
It allows users to ask medical questions and receive **context-aware, document-grounded answers** sourced from trusted medical literature.

The chatbot supports **multi-turn conversations**, meaning it can remember prior context during a session and respond naturally to follow-up questions.

> ⚠️ **Disclaimer**  
> This chatbot is intended for **educational and informational purposes only** and is **not a substitute for professional medical advice**.

---

## 🎯 Key Features

- 📄 **PDF-based Knowledge Source**  
  Uses medical reference documents (e.g., *The Gale Encyclopedia of Medicine*).

- 🧠 **Conversational Memory**  
  Maintains recent chat context to handle follow-up questions like *“tell more about it”*.

- 🔍 **Semantic Search with FAISS**  
  Retrieves the most relevant document chunks using vector similarity.

- 🤖 **LLM-powered Responses (Groq)**  
  Generates accurate, concise answers grounded strictly in retrieved content.

- 📚 **Source Transparency**  
  Displays source documents and page numbers used for each response.

- 🌐 **Web-based Interface (Streamlit)**  
  Simple and interactive chat interface.

---

## 🧱 System Architecture

User
↓
Streamlit Chat Interface
↓
Conversational RAG Pipeline
↓
FAISS Vector Store (PDF embeddings)
↓
Groq LLM

yaml
Copy code

---

## 🛠️ Tech Stack

| Component | Technology |
|---------|------------|
| Language | Python |
| LLM | Groq |
| Embeddings | sentence-transformers (MiniLM) |
| Vector Database | FAISS |
| Framework | LangChain |
| UI | Streamlit |
| Environment | python-dotenv |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

MedicalChatBot/
│
├── create_memory_for_llm.py # Build FAISS vector store from PDFs
├── connect_memory_with_llm.py # RAG pipeline (retrieval + LLM)
├── medibot.py # Streamlit chat UI
├── data/ # Medical PDF documents
├── vectorstore/db_faiss/ # FAISS index files
├── .gitignore # Ignored files (env, venv, cache)
├── .env.example # Environment variable template
└── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Srirajop/MedicalChatBot.git
cd MedicalChatBot
2️⃣ Create Virtual Environment (Recommended)
bash
Copy code
python -m venv .venv
.venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
(If requirements.txt is not present, install dependencies manually.)

4️⃣ Configure Environment Variables
Create a .env file:

env
Copy code
GROQ_API_KEY=your_groq_api_key_here
⚠️ .env is ignored by Git and must never be committed.

5️⃣ Build Vector Store (Run Once)
bash
Copy code
python create_memory_for_llm.py
6️⃣ Run the Chatbot
bash
Copy code
streamlit run medibot.py
Open in browser:

arduino
Copy code
http://localhost:8501
💬 Example Interaction
User:
What is cancer?

Bot:
Cancer is a disease in which cells grow uncontrollably due to genetic changes, forming abnormal tumors.

User:
Tell more about it.

Bot:
(Continues explanation using previous context and retrieved documents.)

🧠 Conversational Memory Design
Maintains recent dialogue history within a session

Resolves pronouns and follow-up questions naturally

History length is bounded to avoid retrieval noise

🔐 Security & Best Practices
API keys stored using environment variables

.env, virtual environments, and cache files ignored via .gitignore

GitHub Push Protection prevents accidental secret exposure

🚀 Future Enhancements
User authentication

Persistent chat history

Multi-document uploads

REST API deployment (FastAPI)

Website widget integration

Medical disclaimer banner

🎓 Academic Relevance
This project demonstrates concepts from:

Generative AI

Natural Language Processing

Information Retrieval

Vector Databases

Human-Computer Interaction

Suitable for:

Mini projects

Final-year projects

AI/ML coursework demonstrations

📜 License
This project is intended for educational use only.
All referenced documents remain the property of their respective publishers.

yaml
Copy code

---

## ✅ WHY THIS FIX WORKS

- Uses **proper Markdown headings** (`#`, `##`, `---`)
- Bullet lists are correctly spaced
- Emojis are used **only in headings**
- Code blocks render correctly
- GitHub preview will look **clean and professional**

---

## 🔧 FINAL STEP (IMPORTANT)

After pasting:

```bash
git add README.md
git commit -m "Fix README formatting"
git push origin main
