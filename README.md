# VectorLess RAG Using PageIndex

A Vectorless RAG (Retrieval-Augmented Generation) chatbot built using:

- [PageIndex](https://pageindex.ai)
- [FastAPI](https://fastapi.tiangolo.com)
- [Streamlit](https://streamlit.io)
- [Google AI Studio](https://aistudio.google.com)

This project allows users to:

- Upload PDF documents
- Extract and index document content using PageIndex
- Ask questions from uploaded documents
- Get context-aware answers without using vector databases

---

# Features

- PDF Upload Support
- Vectorless RAG Architecture
- FastAPI Backend
- Streamlit Frontend
- Google Gemini Integration
- PageIndex Document Search
- Swagger UI Support

---

# Project Structure

```txt
VectorLess_RAG_Using_PageIndex/
│
├── backend/
│   ├── app/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   └── app.py
│
├── .env
├── .gitignore
└── README.md
```

---

# Frontend Features

The Streamlit frontend provides two main options:

## 1. Upload PDF

Users can upload a PDF document.

After upload:
- PageIndex processes the document
- A `DOC_ID` is generated
- Copy this `DOC_ID`
- Add it to the `.env` file

---

## 2. Ask Query

Users can ask questions related to the uploaded PDF.

The chatbot retrieves relevant document chunks using PageIndex and generates answers using Gemini.

---

# Backend API Endpoints

## Upload PDF Endpoint

```http
POST /upload_pdf
```

Used for:
- Uploading PDFs
- Sending files to PageIndex
- Getting `DOC_ID`

---

## Query Endpoint

```http
POST /query
```

Used for:
- Asking questions
- Retrieving document context
- Generating final answer

---

# Environment Variables

Create a `.env` file in the project root.

## `.env`

```env
GOOGLE_API_KEY=your_google_api_key
PAGEINDEX_API_KEY=your_pageindex_api_key
DOC_ID=your_uploaded_document_id
```

---

# How to Get API Keys

## 1. Google API Key

### Steps

1. Open:
   https://aistudio.google.com

2. Login with your Google account

3. Click:
   - "Get API Key"

4. Create API key

5. Copy and add it to `.env`

Example:

```env
GOOGLE_API_KEY=AIza....
```

---

## 2. PageIndex API Key

### Steps

1. Open:
   https://pageindex.ai

2. Create account / Login

3. Open dashboard

4. Generate API key

5. Copy and add it to `.env`

Example:

```env
PAGEINDEX_API_KEY=pi_....
```

---

# Important Note for New Users

Before asking queries:

- Upload at least one PDF first
- Copy generated `DOC_ID`
- Add it inside `.env`

Example:

```env
DOC_ID=abc123xyz
```

---

# Installation Steps

## 1. Clone Repository

```bash
git clone https://github.com/Mit-007/VectorLess_RAG_Using_PageIndex.git
```

---

## 2. Move Into Project Folder

```bash
cd VectorLess_RAG_Using_PageIndex
```

---

# Backend Setup

## 3. Create Virtual Environment

### Windows

```bash
python -m venv myvenv
```

---

## 4. Activate Virtual Environment

### Windows

```bash
myvenv\Scripts\activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6. Create `.env` File

Add:

```env
GOOGLE_API_KEY=your_google_api_key
PAGEINDEX_API_KEY=your_pageindex_api_key
DOC_ID=your_doc_id
```

---

# Run Backend Server

## 7. Start FastAPI Server

```bash
cd backend
uvicorn app.main:app --reload
```

Server runs on:

```txt
http://127.0.0.1:8000
```

---

# Swagger UI

Open:

```txt
http://127.0.0.1:8000/docs
```

Swagger UI allows:
- Testing APIs
- Uploading PDFs
- Running queries

---

# Run Streamlit Frontend

## 8. Start Frontend

Open a new terminal and run:

```bash
streamlit run frontend/app.py
```

Frontend runs on:

```txt
http://localhost:8501
```

---

# Workflow

## Step 1
Run backend server.

## Step 2
Run Streamlit frontend.

## Step 3
Upload PDF.

## Step 4
Copy generated `DOC_ID`.

## Step 5
Add `DOC_ID` to `.env`.

## Step 6
Restart backend server.

## Step 7
Ask questions from uploaded PDF.

---

# Technologies Used

- Python
- FastAPI
- Streamlit
- Google Gemini
- PageIndex

---

# Repository

GitHub Repository:
https://github.com/Mit-007/VectorLess_RAG_Using_PageIndex

---

# Author

Developed by MIT-007