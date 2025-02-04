### 📄 **README.md for Faculty RAG Chatbot Project**

---

# 🎓 **Faculty RAG Chatbot**  
An AI-powered chatbot that helps students find information about their college faculty, including specializations, emails, and more. This project uses **RAG (Retrieval-Augmented Generation)** with **LangChain**, **Google Gemini API**, **FastAPI**, **LangSmith**, and **Streamlit**.

---

## 🚀 **Features**  
- 🤖 Multi-user support  
- 🔍 Retrieve faculty details (specialization, email, etc.)  
- 💬 Conversational memory (understands follow-up questions)  
- 📊 Uses CSV data for faculty information  
- 🌐 Integrated with Google Gemini LLM  
- 🔗 Backend (FastAPI) + Frontend (Streamlit)  

---

## ⚙️ **Tech Stack**  
- **Backend:** FastAPI, LangChain, LangSmith, Google Gemini API  
- **Frontend:** Streamlit  
- **Database:** Vector Store (for embeddings), CSV (for faculty data)  

---

## 📁 **Project Structure**  
```
faculty-rag-chatbot/
├── app/                        
│   ├── main.py                # FastAPI backend
│   ├── vector_store/          # Saved vector database
│   └── data/faculty.csv       # Faculty data (CSV)
├── frontend/                  
│   └── app.py                 # Streamlit frontend
├── requirements.txt           # Python dependencies
├── .env                       # API keys (hidden)
├── Procfile                   # For deployment (Render)
└── README.md                  # Project documentation
```

---

## 🚨 **Prerequisites**  
- Python 3.9+  
- Google Gemini API Key  
- LangSmith Account  

---

## 🔑 **Environment Setup**  
1. **Clone the repository:**  
   ```bash
   git clone https://github.com/your-username/faculty-rag-chatbot.git
   cd faculty-rag-chatbot
   ```

2. **Create a virtual environment:**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**  
   Create a `.env` file:  
   ```
   GEMINI_API_KEY=your_gemini_api_key
   LANGCHAIN_API_KEY=your_langchain_api_key
   LANGSMITH_API_KEY=your_langsmith_api_key
   ```

---

## 🚀 **Run the Project Locally**  

1. **Start the FastAPI Backend:**  
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Run the Streamlit Frontend:**  
   ```bash
   cd frontend
   streamlit run app.py
   ```

3. **Access the App:**  
   Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🌐 **Deployment Instructions**  

### 1️⃣ **Deploy FastAPI on Render**  
- Push the backend to GitHub  
- Create a new **Web Service** on [Render](https://render.com)  
- Add the **Procfile** for deployment  
- Set environment variables in Render dashboard  

### 2️⃣ **Deploy Streamlit on Streamlit Cloud**  
- Push the frontend code to GitHub  
- Go to [Streamlit Cloud](https://streamlit.io/cloud)  
- Click **"New app"**, select your repo, and deploy  

---

## ❓ **How It Works**  
- **Query:** Users submit questions about faculty.  
- **Retrieval:** The backend fetches relevant info from the CSV.  
- **Embedding:** Data is embedded using Google Gemini.  
- **Response:** LangChain + LangSmith handle the AI responses.  

---

## 💡 **Sample Questions**  
- *"Who is the best teacher for Machine Learning?"*  
- *"What is his email?"* (The bot remembers context!)  
- *"Which faculty specializes in Data Science?"*  

---

## 🤝 **Contributing**  
1. Fork this repo  
2. Create a new branch  
3. Make your changes  
4. Submit a pull request  

---

## 📜 **License**  
This project is licensed under the MIT License.  

Let me know if you'd like to tweak anything! 🚀
