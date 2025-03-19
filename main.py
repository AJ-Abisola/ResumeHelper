import PyPDF2
import pdfplumber
import spacy
from spacy.matcher import PhraseMatcher

class resume_helper:
    # Skills List
    data_ml_skills = [
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
        "Professional Certificate"]

    courses = [
        "Computer Science", "Data Science", "Machine Learning", "Artificial Intelligence",
        "Statistics", "Mathematics", "Business Analytics", "Information Technology",
        "Software Engineering", "Computational Science", "Operations Research"
    ]

    def __init__(self,path):
        self.path = path
        self.nlp = spacy.load("en_core_web_sm")
        self.matcher = PhraseMatcher(self.nlp.vocab, attr="LOWER")
        self.text = self.extract_text()
        # self.text = "Experienced in Python, TensorFlow, AWS, and Docker for machine learning workflows. MBA from Havard"
        self.doc = self.nlp(self.text)
        self.educations_found = self.matcher_func(self.education)
        self.skills_found = self.matcher_func(self.data_ml_skills)
        print("Skills found:", self.skills_found)
        print("Education found:", self.educations_found)

    def extract_text(self):
        text = ""
        with pdfplumber.open(self.path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text


    def matcher_func(self, pattern_array):
        patterns = [self.nlp.make_doc(pattern) for pattern in pattern_array]
        self.matcher.add("latest_pattern", None, *patterns)
        patterns_found = self.extract_pattern()
        self.matcher.remove("latest_pattern")

        return patterns_found

    def extract_pattern(self):

        matches = self.matcher(self.doc)

        found_patterns = set()

        for match_id, start, end in matches:
            span = self.doc[start:end]
            found_patterns.add(span.text)

        return list(found_patterns)


if __name__ == "__main__":
    path = "pdf_path"
    parser = resume_helper(path)