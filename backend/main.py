from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import CSVLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langsmith import Client
import os
import uvicorn
from dotenv import load_dotenv

load_dotenv()
# Set environment variables
GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"] 
LANGSMITH_API_KEY=os.environ["LANGSMITH_API_KEY"]
os.environ["LANGSMITH_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Faculty Chatbot"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"

# Check for LangSmith API key
api_key = os.getenv("LANGSMITH_API_KEY")
if not api_key:
    raise ValueError("LangSmith API key is missing. Set LANGSMITH_API_KEY as an environment variable.")

# Initialize LangSmith client
client = Client()

# Load data into vectorstore
def load_data_to_vectorstore():
    try:
        loader = CSVLoader(file_path= r"C:\Users\Anvay\OneDrive\Desktop\FacultyRAG\Faculty details sample.csv")  # Update path to your CSV file
        documents = loader.load()
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vectorstore = FAISS.from_documents(documents, embeddings)
        vectorstore.save_local("vector_store")
        print("Vectorstore saved.")
        return vectorstore
    except Exception as e:
        print(f"Error loading data to vectorstore: {e}")
        raise

vectorstore = load_data_to_vectorstore()

# Initialize memory and LLM
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
google_llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# Create conversational retrieval chain
chat_chain = ConversationalRetrievalChain.from_llm(
    llm=google_llm,
    retriever=vectorstore.as_retriever(),
    memory=memory,
    
)

# Create FastAPI app
app = FastAPI()

class ChatRequest(BaseModel):
    user_id: str
    question: str

@app.post("/query")
async def query_chatbot(request: ChatRequest):
    user_id = request.user_id
    question = request.question

    run = None

    try:
        run = client.create_run(
            name="faculty_chatbot_run",
            inputs={"user_id": user_id, "question": question},
            run_type="chain",
            metadata={"user_id": user_id}
        )

        response = chat_chain({"question": question})
        if run:
            client.update_run(run["id"], outputs={"answer": response["answer"]})
        return {"answer": response["answer"]}

    except Exception as e:
        if run:
            client.update_run(run["id"], error=str(e))
        return {"error": str(e)}

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

# Run FastAPI
import nest_asyncio
nest_asyncio.apply()
uvicorn.run(app, host="127.0.0.1", port=8000)