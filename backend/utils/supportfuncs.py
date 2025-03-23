import re
import dateparser
from datetime import datetime
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_similarity(resume_resp, jd_text):
    embeddings = model.encode([resume_resp, jd_text], convert_to_tensor=True)
    similarity_score = util.pytorch_cos_sim(embeddings[0], embeddings[1])

    return float(similarity_score)

def parse_date(date_str):
    """Parses a date string into a datetime object."""
    if not date_str or date_str.lower() in ['present', 'current']:
        return datetime.now()
    return dateparser.parse(date_str)


def total_experience(jobs):
    """Calculates total years of experience from job date ranges."""
    total_days = 0

    for job in jobs:
        if 'dates' not in job or len(job['dates']) < 2:
            continue

        start_str, end_str = job['dates'][0], job['dates'][1]

        start_date = parse_date(start_str)
        end_date = parse_date(end_str)

        if not start_date or not end_date:
            continue

        delta = end_date - start_date
        total_days += delta.days

    # Convert days to years (roughly)
    total_years = total_days / 365
    return round(total_years, 2)


def max_years_jd(jd_text):
    # Matches patterns like "3+ years", "5 years", "10+ yrs"
    matches = re.findall(r'(\d+)\s*\+?\s*(years|yrs)', jd_text.lower())
    years_list = [int(year[0]) for year in matches]

    if years_list:
        return max(years_list)
    return 0

def resume_responsibilities(jobs):
    all_responsibilities = ""

    for job in jobs:
        responsibilities = job.get('responsibilities', '')
        all_responsibilities += responsibilities + " "

    return all_responsibilities.strip()

