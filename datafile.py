import re



job_titles = [
    # Core Data Roles
    "Data Scientist",
    "Senior Data Scientist",
    "Lead Data Scientist",
    "Junior Data Scientist",
    "Data Analyst",
    "Business Data Analyst",
    "Senior Data Analyst",
    "Quantitative Analyst",
    "Data Engineer",
    "Senior Data Engineer",
    "Big Data Engineer",
    "Data Platform Engineer",

    # Machine Learning
    "Machine Learning Engineer",
    "Senior Machine Learning Engineer",
    "ML Engineer",
    "Applied Machine Learning Scientist",
    "Machine Learning Scientist",
    "Deep Learning Engineer",
    "Deep Learning Scientist",

    # AI-Specific
    "AI Engineer",
    "Artificial Intelligence Engineer",
    "AI Specialist",
    "AI Software Engineer",
    "AI Solutions Architect",
    "AI Research Scientist",
    "AI Developer",
    "Cognitive Computing Engineer",

    # NLP and Computer Vision
    "NLP Engineer",
    "NLP Scientist",
    "Computer Vision Engineer",
    "Computer Vision Scientist",
    "Speech Recognition Engineer",

    # MLOps and Deployment
    "MLOps Engineer",
    "ML Infrastructure Engineer",
    "DataOps Engineer",
    "ML Platform Engineer",

    # Analytics & BI
    "Data Analytics Consultant",
    "Business Intelligence Developer",
    "BI Analyst",
    "BI Developer",

    # Leadership
    "Head of Data Science",
    "Chief Data Scientist",
    "Director of Data Science",
    "Director of AI",
    "AI Program Manager",

    # Hybrid/Related Titles
    "Data Architect",
    "Analytics Engineer",
    "Statistical Programmer",
    "Data Visualization Engineer",
    "Decision Scientist",
    "Predictive Modeler",
    "Quantitative Researcher",
    "Research Scientist (AI/ML)"
]

skills = [
        "Python", "R", "SQL", "Java", "Scala", "Julia", "C++", "MATLAB",
        "Apache Spark", "Apache Kafka", "Apache Airflow", "Hadoop", "Databricks", "Flink",
        "ETL", "Snowflake", "Redshift", "BigQuery", "Data Warehouse", "Data Lake", "Amazon S3",
        "TensorFlow", "PyTorch", "Keras", "Scikit-learn", "XGBoost", "LightGBM", "CatBoost",
        "Hugging Face Transformers", "OpenCV", "FastAI",
        "NLTK", "spaCy", "BERT", "GPT", "T5", "Named Entity Recognition", "Topic Modeling",
        "Word2Vec", "Doc2Vec",
        "MLflow", "Kubeflow", "Docker", "Kubernetes", "TensorFlow Serving", "TorchServe", "ONNX",
        "REST APIs", "FastAPI", "Flask", "Airflow",
        "CI/CD", "AWS", "Azure", "Google Cloud Platform", "Amazon SageMaker", "Google AI Platform",
        "Azure Machine Learning", "Lambda", "Cloud Functions", "EC2", "IAM", "S3", "BigQuery",
        "PostgreSQL", "MySQL", "MongoDB", "Cassandra", "Redis", "HDFS", "Neo4j", "ElasticSearch",
        "Tableau", "Power BI", "Looker", "Matplotlib", "Seaborn", "Plotly", "D3.js",
        "Linear Regression", "Logistic Regression", "Hypothesis Testing", "Time Series Analysis",
        "A/B Testing", "Bayesian Statistics", "Clustering", "PCA", "Deep Learning",
        "Reinforcement Learning", "Git", "GitHub", "GitLab", "Bitbucket", "Jira", "Confluence"
]

    # Education List
education = [
        "Bachelor of Science", "Bachelor of Arts", "BSc", "BA", "B.Tech", "BEng", "Bachelor’s Degree",
        "Master of Science", "MSc", "MS", "Master of Engineering", "MEng", "Master of Technology",
        "M.Tech", "Master of Business Administration", "MBA", "Master’s Degree",
        "Doctor of Philosophy", "PhD", "DPhil", "Doctorate",
        "Postgraduate Diploma", "PGDip", "Graduate Certificate", "Nanodegree",
        "Professional Certificate"
]

courses = [
        "Computer Science", "Data Science", "Machine Learning", "Artificial Intelligence",
        "Statistics", "Mathematics", "Business Analytics", "Information Technology",
        "Software Engineering", "Computational Science", "Operations Research"
]

other_sections = [
    # Education related
    "Education",
    "Academic Background",
    "Educational Qualifications",
    "Academic History",
    "Educational Background",
    "Academic Experience",

    # Skills related
    "Skills",
    "Technical Skills",
    "Core Competencies",
    "Key Skills",
    "Areas of Expertise",

    # Certifications
    "Certifications",
    "Licenses",
    "Professional Certifications",
    "Certifications and Licenses",

    # Projects and Publications
    "Projects",
    "Research Projects",
    "Publications",
    "Research and Publications",

    # Awards and Achievements
    "Awards",
    "Honors and Awards",
    "Achievements",
    "Recognitions",

    # Volunteer/Extracurricular
    "Volunteer Experience",
    "Community Involvement",
    "Extracurricular Activities",

    # Languages
    "Languages",
    "Language Proficiency",

    # References
    "References",
    "Professional References",

    # Hobbies (less common, but possible)
    "Hobbies",
    "Interests",
    "Personal Interests",

    # Summary/Objective (sometimes appears later)
    "Summary",
    "Professional Summary",
    "Career Objective",
    "Objective",

    # Personal Information (rare)
    "Personal Information",
    "Contact Information"
]


work_section = [
    "Work Experience",
    "Professional Experience",
    "Employment History",
    "Career History",
    "Experience",
    "Professional Background",
    "Relevant Experience",
    "Employment Experience",
    "Work History",
    "Professional Work History",
    "Job Experience",
    "Work Summary",
    "Experience Summary",
    "Career Experience",
    "Career Summary"
]

date_patterns = [
    # Month + Year (e.g., Jan 2023 or January 2023)
    r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{4}",

    # Year Only (e.g., 2023)
    r"\b\d{4}\b",

    # Month Year - Month Year range (e.g., Jan 2022 - Mar 2023)
    r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{4}\s*(?:–|-|to)\s*(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{4}",

    # Formats like MM/YYYY or M/YYYY
    r"\b\d{1,2}/\d{4}\b",

    # Present terms
    r"\bPresent\b|\bCurrent\b"
]

date_regex = re.compile('|'.join(date_patterns), flags=re.IGNORECASE)
