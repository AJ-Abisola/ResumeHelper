import streamlit as st
import requests
import os
import time

# Backend URL
# BACKEND_URL = "http://localhost:8000/compare"
BACKEND_URL = "http://backend:8000/compare"

st.set_page_config(page_title="Resume Matcher", layout="wide")
st.title("🚀 Resume vs Job Description Matcher")

# Initialize session state
if "phase" not in st.session_state:
    st.session_state.phase = "input"
# Initialize session state for results
if "results" not in st.session_state:
    st.session_state["results"] = None

# def save_uploaded_file(uploaded_file, save_path):
#     with open(save_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())

def show_upload_page():
    with st.form("resume_form"):
        # File uploader
        resume_file = st.file_uploader("Upload your Resume", type=["pdf"])
        jd = st.text_area("Paste the Job Description")
        submitted = st.form_submit_button("Compare!")

        time.sleep(5)
        if submitted:

            if resume_file and jd:

                st.write(f"You wrote {len(jd)} characters.")

                with st.spinner("Analyzing..."):

                    # Send files to backend
                    files = {
                        "resume": resume_file
                    }

                    data = {
                        "jd": jd
                    }

                    try:
                        response = requests.post(BACKEND_URL, files=files, data=data)

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
                    except requests.exceptions.ConnectionError:
                        st.error("Could not connect to backend service. Please try again later.")
                        st.rerun()

                    except requests.exceptions.Timeout:
                        st.error("Backend service timed out. Please try again later.")
                        st.rerun()

                    except Exception as e:
                        st.error(f"An unexpected error occurred: {str(e)}")
                        st.rerun()

            else:
                st.error("Please upload resume and paste the job description")

        else:
            st.warning("Both Resume and JD are required.")



if __name__ == "__main__":
    show_upload_page()


