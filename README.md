## 📄 Resume Parser & Job Matcher

A Resume Parser & Job Recommendation System, designed to extract key information from resumes (Skills, Education, Experience), compare them with job descriptions, and provide feedback to optimize candidate-job alignment.

---

### 🚀 Features

- Resume Parsing using spaCy and pdfplumber
- NLP-based Job Description analysis using sentence-transformers
- Semantic Similarity Scoring between Resume & Job Description
- Skill Gap Analysis
- Clean Streamlit Frontend
- FastAPI Backend with RESTful API
- Fully containerized with Docker & Docker Compose
- AWS EC2 Deployment Ready!

---

### 🛠️ Tech Stack

Frontend |	Backend |	AI/ML & NLP	| Infrastructure
|---|---|---|---|
Streamlit | FastAPI	| spaCy, Sentence Transformers, pdfplumber, dateparser	| Docker, Docker Compose, AWS EC2

---
### 🔧 Local Setup & Installation

1. Clone the repo and cd into the folder
    
```bash
    git clone https://github.com/AJ-Abisola/ResumeHelper.git
    cd ResumeHelper
   ```

2. Environment Prerequisites
   - Docker & Docker Compose installed
   - Python 3.10+ (if not using Docker)
---   

### 🐳 Docker Setup (Recommended)

**1. Build & Run the Containers**
```bash
  docker-compose up --build -d
```
**2. Access the App**

Go to:

```bash
    http://localhost:8501
   ```
For deployed servers (e.g., EC2):

```bash
    http://<your-ec2-public-ip>:8501
```
---

### Manual Local Setup (Non-Docker)

#### Backend (FastAPI)
```bash
    cd backend
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python -m spacy download en_core_web_sm
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
#### Frontend (Streamlit)
```bash
    cd frontend
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    streamlit run app.py --server.port=8501 --client.sidebarNavigation False
```

---

#### ⚙️ API Endpoints (Backend)

Method | Endpoint | Description
|---|---|---|
POST | /compare | Compares resume with job description and returns feedback

#### Sample Request
```bash
    POST /compare
    Form Data:
    - resume (file)
    - jd_text (text)
```

---

### Potential Improvements
- Add more fields. Right now, it only handles the field of data - data scientist, ML engineer, AI engineer etc.
- Real-time job scraping from LinkedIn / Indeed APIs
- Fine-tune semantic similarity thresholds by comparing individually instead of as a whole.
- Add PDF Report Generation
- Add User Profiles for multiple resumes
