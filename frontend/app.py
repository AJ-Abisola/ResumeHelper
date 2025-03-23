import streamlit as st
import requests
import os

# Backend URL
BACKEND_URL = "http://localhost:8000/compare"


st.set_page_config(page_title="Resume Matcher", layout="wide")
st.title("🚀 Resume vs Job Description Matcher")

# Initialize session state
if "phase" not in st.session_state:
    st.session_state.phase = "input"
# Initialize session state for results
if "results" not in st.session_state:
    st.session_state["results"] = None

def save_uploaded_file(uploaded_file, save_path):
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

def show_upload_page():
    with st.form("resume_form"):
        # File uploader
        resume_file = st.file_uploader("Upload your Resume", type=["pdf"])
        jd = st.text_area("Paste the Job Description")

        if st.form_submit_button("Compare!"):

            if resume_file and jd:

                st.write(f"You wrote {len(jd)} characters.")

                with st.spinner("Analyzing..."):
                    path = "/Users/ajabisola/Documents/projects/resume_parser/backend/models/temp"
                    if not os.path.exists(path):
                        os.makedirs(path)

                    # Save uploaded files
                    resume_path = f"{path}/{resume_file.name}"
                    save_uploaded_file(resume_file, resume_path)

                    # Send files to backend
                    files = {
                        "resume": resume_path,
                        "jd": jd
                    }

                    response = requests.post(BACKEND_URL, data=files)

                    if response.status_code == 200:
                        st.session_state.results = response.json()
                        st.session_state.phase = "results"
                        if st.session_state["results"] and st.session_state.phase == "results":
                            # show_result_page()
                            st.switch_page("pages/results.py")
                    else:
                        st.error(f"Error {response.status_code}: Something went wrong! Try again.")
                        st.session_state.phase = "input"
                        st.rerun()

            else:
                st.error("Please upload resume and paste the job description")

        else:
            st.warning("Both Resume and JD are required.")



if __name__ == "__main__":
    show_upload_page()


