#Setup LLM Mistral with HuggingFace
#Connect LLM with FAISS
#Create Chain
#Setup LLM Mistral with HuggingFace
#Connect LLM with FAISS
#Create Chain
import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

_rag_chain = None
_retriever = None

def _build_backend():
    global _rag_chain, _retriever

    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.1-8b-instant",
        temperature=0.3
    )

    prompt = PromptTemplate(
        template="""
Use the pieces of information provided in the context to answer user's question.
If you dont know the answer, just say that you dont know, dont try to make up an answer.
Do NOT explain where the information comes from the books pdfs sources texts or documents.
Speak as if you already know the information naturally.
If the answer is not clearly stated, say: "I do not know."

Context:
{context}

Question:
{question}

Answer:
""",
        input_variables=["context", "question"]
    )

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.load_local(
        "vectorstore/db_faiss",
        embedding_model,
        allow_dangerous_deserialization=True
    )

    _retriever = db.as_retriever(search_kwargs={"k": 5})

    _rag_chain = (
        {
            "context": _retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
    )

def get_answer_and_sources(query: str):
    global _rag_chain, _retriever

    if _rag_chain is None:
        _build_backend()

    docs = _retriever.invoke(query)
    answer = _rag_chain.invoke(query).content.strip()

    sources = [
        f"{doc.metadata.get('source')} (page {doc.metadata.get('page')})"
        for doc in docs
    ]

    return answer, sources