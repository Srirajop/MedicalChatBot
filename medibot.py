import streamlit as st
from connect_memory_with_llm import get_answer_and_sources

st.set_page_config(page_title="MediBot", page_icon="🩺")

MAX_HISTORY = 4  # last 4 exchanges only (safe for medical RAG)

def format_chat_history(messages):
    history = []
    for msg in messages[-MAX_HISTORY * 2:]:
        role = "User" if msg["role"] == "user" else "Assistant"
        history.append(f"{role}: {msg['content']}")
    return "\n".join(history)


def main():
    st.title("🩺 Ask ChatBot")

    if "messages" not in st.session_state:
        st.session_state.messages = []

        # Initial greeting
        st.session_state.messages.append({
            "role": "assistant",
            "content": "Hello, I am MediBot. How can I help you today?"
        })

    # Show chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_input = st.chat_input("Ask a medical question")

    if user_input:
        with st.chat_message("user"):
            st.markdown(user_input)

        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        # 🔑 Build conversational query
        chat_history = format_chat_history(st.session_state.messages)

        conversational_query = f"""
Conversation so far:
{chat_history}

Current question:
{user_input}
"""

        with st.spinner("Thinking..."):
            answer, sources = get_answer_and_sources(conversational_query)

        with st.chat_message("assistant"):
            st.markdown(answer)

            with st.expander("Source Documents"):
                for src in sources:
                    st.markdown(f"- {src}")

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )


if __name__ == "__main__":
    main()

