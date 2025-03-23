from parser import parser
import supportfuncs

def feedback_generator():

    resume = parser(path)
    jd = parser(text=jd_text)
    feedback = {}

    resume_education = resume.extract_pattern("education")[0]
    resume_skills = resume.extract_pattern("skills")[0]
    resume.extract_responsibilities()

    jd_education = jd.extract_pattern("education")[0]
    jd_skills = jd.extract_pattern("skills")[0]

    # Education comparison and suggestion
    education_feedback = {
        "resume_education": resume_education,
        "jd_education": jd_education
    }
    if jd_education:
        education_match = bool(set(resume_education).intersection(jd_education))
        if not education_match:
            education_suggestion = (
                f"You seem to not have the required degree listed in the job description. {', '.join(jd_education)} is missing on resume"
            )
        else:
            education_suggestion = "You meet the education requirement."

        feedback["education"] = {
            "analysis": education_feedback,
            "suggestion": education_suggestion
        }

    else:
        feedback["education"] = {
            "analysis": education_feedback,
            "suggestion": "No relevant education mentioned in the Job description. You may qualify for the minimum requirement."
        }

    # Skills comparison and suggestion
    matched_skills = list(set(resume_skills).intersection(jd_skills))
    missing_skills = list(set(jd_skills).difference(resume_skills))
    skills_feedback = {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }

    if missing_skills:
        skills_suggestion = (
            f"Consider adding projects or experience that demonstrate your skills in: {', '.join(missing_skills)}."
        )
    else:
        skills_suggestion = "You meet the required skills listed in the job description."

    feedback["skills"] = {
        "analysis": skills_feedback,
        "suggestion": skills_suggestion
    }

    # Years of experience comparison and suggestion
    resume_yoe = supportfuncs.total_experience(resume.jobs_found)
    jd_yoe = supportfuncs.max_years_jd(jd_text)

    if resume_yoe >= jd_yoe:
        exp_feedback = (
            f"You have {resume_yoe} year(s) of experience, which meets the requirement of {jd_yoe} year(s)."
        )
    else:
        exp_feedback = (
            f"The job requires {jd_yoe} year(s) of experience, but your resume shows {resume_yoe} year(s). "
            "Consider emphasizing relevant projects or roles to bridge this gap."
        )

    feedback["experience"] = {
        "resume_years": resume_yoe,
        "required_years": jd_yoe,
        "suggestion": exp_feedback
    }

    # Responsibilities comparison and suggestion
    resume_responsibilities = supportfuncs.resume_responsibilities(resume.jobs_found)
    jd_responsibilities = jd_text
    resp_similarity = supportfuncs.semantic_similarity(resume_responsibilities, jd_responsibilities)

    if resp_similarity >= 0.85:
        resp_feedback = "Your responsibilities align well with the role."
    elif 0.7 <= resp_similarity < 0.85:
        resp_feedback = (
            "Your responsibilities are a decent match, but you can improve alignment by emphasizing outcomes "
            "or metrics that relate to the job description."
        )
    else:
        resp_feedback = (
            "The responsibilities listed in your resume do not clearly align with the job. "
            "Consider rephrasing your experience to focus on key tasks and achievements mentioned in the JD."
        )

    feedback["responsibilities"] = {
        "similarity_score": round(resp_similarity, 2),
        "suggestion": resp_feedback
    }

    return feedback


if __name__ == "__main__":
    # path = "pdf_path"
    path = "/Users/ajabisola/Documents/CVs/JA.pdf"
    jd_text = '''
    Dive deep into Digital! For 20 years Intellias has been developing top-tier digital solutions for the world’s leading companies, keeping them in line with the latest technology trends. Join in and provide innovations for the future!
    Project Overview:
    We are seeking a Data Scientist with expertise in machine learning, large language models (LLMs), and AI-driven solutions. The ideal candidate will have a strong foundation in traditional statistical models and machine learning techniques, coupled with hands-on experience in LLM development and prompt engineering. This role requires technical proficiency in Python, Docker, and GitLab CI/CD, with a preference for experience in FastAPI. We value individuals who take initiative, demonstrate great work ethics, and focus on the overall success of projects.
    Requirements:
    Strong understanding of machine learning models, statistical analysis, and data science principles.
    GCP proficiency is a must
    Hands-on experience with LLMs, prompt engineering, and AI model optimization.
    Proficiency in Python, Docker, and GitLab CI/CD for data science workflows.
    (Preferred) Experience with FastAPI for API development and deployment.
    Strong problem-solving skills and a proactive approach to project execution.
    Excellent teamwork, communication, and initiative in delivering impactful solutions.
    Ability to work EST hours

    Responsibilities:
    Develop, train, and optimize traditional machine learning models for data analysis and predictive insights.
    Apply expertise in LLMs and prompt engineering to create and refine AI-driven applications.
    Utilize Python, Docker, and GitLab CI/CD for model development, automation, and deployment.
    (Preferred) Implement FastAPI for building scalable APIs and integrating machine learning models into production environments.
    Collaborate with cross-functional teams to drive AI-powered innovations and ensure project success.
    Maintain a high standard of coding practices, version control, and model performance evaluation.
    '''
    feedback = feedback_generator()
    print(feedback['education']['suggestion'])
    print(feedback['skills']['suggestion'])
    print(feedback['experience']['suggestion'])
    print(feedback['responsibilities']['suggestion'])
