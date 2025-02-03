import streamlit as st
import requests

# FastAPI backend URL
FASTAPI_URL = "http://127.0.0.1:8000"  # Update if FastAPI is hosted elsewhere

# Streamlit app title
st.title("Faculty Chatbot")

# User input
user_id = st.text_input("Enter your User ID:", value="user123")
question = st.text_input("Enter your question:")

# Button to send query
if st.button("Ask"):
    if not user_id or not question:
        st.error("Please enter both User ID and a question.")
    else:
        # Send request to FastAPI backend
        try:
            response = requests.post(
                f"{FASTAPI_URL}/query",
                json={"user_id": user_id, "question": question}
            )
            if response.status_code == 200:
                st.success("Response from Chatbot:")
                st.write(response.json().get("answer", "No answer found."))
            else:
                st.error(f"Error: {response.json().get('error', 'Unknown error')}")
        except Exception as e:
            st.error(f"Failed to connect to the backend: {e}")


