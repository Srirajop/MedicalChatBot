🩺 MedicalChatBot – Conversational RAG-based Medical Assistant
📌 Project Overview

MedicalChatBot is a conversational medical assistant built using Retrieval-Augmented Generation (RAG).
It allows users to ask medical questions and receive context-aware, document-grounded answers sourced from trusted medical literature.

The chatbot supports multi-turn conversations, meaning it can remember prior context during a session and respond naturally to follow-up questions.

⚠️ Disclaimer:
This chatbot is intended for educational and informational purposes only and is not a substitute for professional medical advice.

🎯 Key Features

📄 PDF-based Knowledge Source
Uses medical reference documents (e.g., The Gale Encyclopedia of Medicine).

🧠 Conversational Memory
Maintains recent chat context to handle follow-up questions like “tell more about it”.

🔍 Semantic Search with FAISS
Retrieves the most relevant document chunks using vector similarity.

🤖 LLM-powered Responses (Groq)
Generates accurate, concise answers grounded strictly in retrieved content.

📚 Source Transparency
Displays source documents and page numbers used for each response.

🌐 Web-based UI (Streamlit)
Simple and interactive chat interface.

🧱 System Architecture
User (Web UI)
     ↓
Streamlit Chat Interface
     ↓
Conversational RAG Pipeline
     ↓
FAISS Vector Store (PDF embeddings)
     ↓
Groq LLM (Answer Generation)

🛠️ Tech Stack
Component	Technology
Programming Language	Python
LLM Provider	Groq
Embeddings	sentence-transformers (MiniLM)
Vector Database	FAISS
Framework	LangChain
UI	Streamlit
Environment Management	python-dotenv
Version Control	Git & GitHub
📂 Project Structure
MedicalChatBot/
│
├── create_memory_for_llm.py        # Builds FAISS vector store from PDFs
├── connect_memory_with_llm.py      # RAG pipeline (retrieval + LLM)
├── medibot.py                      # Streamlit chat UI
├── data/                           # Medical PDF documents
├── vectorstore/db_faiss/           # FAISS index files
├── .gitignore                      # Ignored files (env, venv, cache)
├── .env.example                    # Environment variable template
└── README.md                       # Project documentation

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/Srirajop/MedicalChatBot.git
cd MedicalChatBot

2️⃣ Create Virtual Environment (Recommended)
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
.venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt


(If requirements.txt is not present, install manually based on imports.)

4️⃣ Configure Environment Variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key_here


⚠️ .env is ignored by Git and should never be committed.

5️⃣ Build Vector Store (Run Once)
python create_memory_for_llm.py


This processes the PDFs and creates FAISS embeddings.

6️⃣ Run the Chatbot
streamlit run medibot.py


Open in browser:

http://localhost:8501

💬 Example Interaction

User:

What is cancer?

Bot:

Cancer is a disease in which cells grow uncontrollably due to genetic changes, forming abnormal masses called tumors.

User:

Tell more about it.

Bot:

(Continues explaining cancer using prior context and retrieved documents.)

🧠 Conversational Memory Design

The chatbot maintains recent dialogue history within the session.

This allows it to resolve pronouns and follow-up questions naturally.

Memory is bounded to avoid retrieval noise and hallucinations.

🔐 Security & Best Practices

API keys are stored using environment variables

.env, virtual environments, and cache files are excluded via .gitignore

GitHub Push Protection prevents accidental secret exposure

🚀 Possible Enhancements

User authentication

Chat history persistence

Multi-document uploads

Deployment as REST API (FastAPI)

Website widget integration

Medical disclaimer banner

👨‍🎓 Academic Use

This project demonstrates concepts from:

Generative AI

Information Retrieval

Natural Language Processing

Vector Databases

Human–Computer Interaction

It is suitable for:

Mini projects

Final year projects

AI/ML coursework demonstrations

📜 License

This project is for educational use.
All referenced documents remain the property of their respective publishers.
