# 🤖 AI PDF Assistant

An AI-powered PDF Question Answering chatbot built using **Google Gemini**, **LangChain**, **FAISS**, and **Sentence Transformers**.

Users can upload any PDF and ask questions in natural language. The chatbot retrieves the most relevant content using Retrieval-Augmented Generation (RAG) and answers only from the uploaded document.

---

## 🚀 Features

- 📄 Upload any PDF
- 💬 Ask questions in natural language
- 🤖 Google Gemini LLM
- 🔍 FAISS Vector Search
- 🧠 Sentence Transformer Embeddings
- 📑 Source Page Citation
- 💾 Download Chat History
- 🎨 Beautiful Streamlit UI

---

## 🛠 Tech Stack

- Python
- Streamlit
- Google Gemini API
- LangChain
- FAISS
- Sentence Transformers
- HuggingFace Embeddings

---

## 📂 Project Structure

```
RAG-ChatBot
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── css/
│
├── data/
│
├── database/
│
└── utils/
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/RAG-ChatBot.git
```

Move into the project

```bash
cd RAG-ChatBot
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

Add screenshots here after deployment.

---

## 🔮 Future Improvements

- Multi-PDF Chat
- Chat Memory
- OCR Support
- Voice Input
- PDF Summarization
- Citation Highlighting

---

