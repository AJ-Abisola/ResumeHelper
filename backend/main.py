from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from typing import Dict
from services.feedback_generator import feedback_generator
import shutil
import os



# Initialize app
app = FastAPI(title="Resume Matcher API")

# CORS for Streamlit (optional for localhost communication)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change later for security!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dummy data for testing
@app.get("/")
def root():
    return {"message": "Resume Matcher Backend is up and running!"}


# Upload Resume and JD files
@app.post("/compare")
async def compare_resume_and_jd(resume: UploadFile = File(...), jd: str = Form(...)) -> Dict:
    path = "temp"
    os.makedirs(path, exist_ok=True)

    # Save uploaded files
    resume_path = os.path.join(path, resume.filename)

    with open(resume_path, "wb") as f:
        shutil.copyfileobj(resume.file, f)

    response = feedback_generator(resume_path,jd)

    return response

# Run the app (For local testing)
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
