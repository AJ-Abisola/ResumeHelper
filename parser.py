import PyPDF2
import pdfplumber
import spacy
from spacy.matcher import PhraseMatcher
import datafile
import re

class parser:

    def __init__(self,path = None,text = None):
        self.path = path
        self.nlp = spacy.load("en_core_web_sm")
        self.matcher = PhraseMatcher(self.nlp.vocab, attr="LOWER")

        if not text:
            self.text = self.extract_text()

        else:
            self.text = text

        self.doc = self.nlp(self.text)

        self.matcher_func("education", datafile.education)
        self.matcher_func("skills", datafile.skills)
        self.matcher_func("job_titles", datafile.job_titles)
        self.matcher_func("work_section", datafile.work_section)
        self.matcher_func("other_sections", datafile.other_sections)

        self.work_section = self.nlp(self.grab_work_section("work_section","other_sections"))

        # self.educations_found = self.extract_pattern("education")[0]
        # self.skills_found = self.extract_pattern("skills")[0]
        self.jobs_found = self.extract_pattern("job_titles", matches=self.matcher(self.work_section))[1]

        # Extract responsibilities for each job
        # self.extract_responsibilities()

        # print("Skills found:", self.skills_found)
        # print("Education found:", self.educations_found)
        # print("Jobs found:", self.jobs_found)

    def extract_text(self):
        text = ""
        with pdfplumber.open(self.path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text(layout=True)
                if page_text:
                    text += page_text + "\n"

        text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)

        # Add space between letters and digits
        text = re.sub(r'([a-zA-Z])(\d)', r'\1 \2', text)
        text = re.sub(r'(\d)([a-zA-Z])', r'\1 \2', text)
        return text

    def extract_dates_from_text(self, text):
        matches = datafile.date_regex.findall(text)
        cleaned_matches = [match for match in matches if match and isinstance(match, str)]
        return cleaned_matches

    def matcher_func(self, match_name: str, pattern_array):

        '''
        Later
        '''
        patterns = [self.nlp.make_doc(pattern) for pattern in pattern_array]
        self.matcher.add(match_name, None, *patterns)

    def extract_pattern(self, match_name, matches=None, window_size=25):

        if not matches:
            matches = self.matcher(self.doc)

        found_patterns = set()
        job_details = []
        self.positions = []

        for match_id, start, end in matches:
            string_id = self.nlp.vocab.strings[match_id]
            if string_id == match_name:

                # Extract the relevant job details
                if match_name == "job_titles":
                    job_title = self.work_section[start:end].text
                    self.positions.append((start, end))
                    window_start = max(0, start - window_size)
                    window_end = min(len(self.doc), end + window_size)

                    context = self.work_section[start:window_end]

                    # Extract dates and org/location from context
                    dates = self.extract_dates_from_text(context.text)
                    orgs = [ent.text for ent in context.ents if ent.label_ in ["ORG", "GPE"]]

                    job_details.append({
                        "job_title": job_title,
                        "organisation/location": orgs,
                        "dates": dates,
                        "start": start,
                        "end": end
                    })

                # Extract other patterns such as skills and education
                else:
                    span = self.doc[start:end]
                    found_patterns.add(span.text)

        return list(found_patterns), job_details

    def extract_responsibilities(self):
        responsibilities = []

        for idx, job in enumerate(self.jobs_found):
            start = job["end"]

            if idx + 1 < len(self.jobs_found):
                end = self.jobs_found[idx + 1]["start"]
            else:
                end = len(self.work_section)

            responsibility_text = self.work_section[start:end].text
            job["responsibilities"] = self.clean_responsibilities(responsibility_text)

    def clean_responsibilities(self, raw_text):
        text = raw_text.strip().replace('\n', ' ').replace('•', ' ').replace('●', ' ').replace('-', ' ')
        text = re.sub(r'\s{2,}', ' ', text)
        text = datafile.date_regex.sub('', text)
        location_pattern = re.compile(
            r',\s*[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?')  # matches something like ", San Francisco" or ", New York"
        text = location_pattern.sub('', text)
        text = re.sub(r'\s{2,}', ' ', text).strip()
        sentences = re.split(r'(?<=[.!?])\s+', text)

        responsibilities = []
        for sent in sentences:
            cleaned = sent.strip(" -●•")
            if len(cleaned) > 3:
                if not cleaned.endswith('.'):
                    cleaned += '.'
                responsibilities.append(cleaned)
        combined_responsibilities = ' '.join(responsibilities)
        return combined_responsibilities

    def grab_work_section(self, start_section, end_section):

        matches = self.matcher(self.doc)
        start_index = None
        end_index = None
        for match_id, start, end in matches:
            string_id = self.nlp.vocab.strings[match_id]
            span = self.doc[start:end]

            if string_id == start_section and start_index is None:
                start = span.end_char  # Where the section starts (after the header)
                start_index = end

            if string_id == end_section and start_index is not None and span.start_char > start:
                end_index = start
                break

        if start_index and end_index:
            return self.doc[start_index:end_index].text
        elif start_index:
            return self.doc[start_index:].text
        else:
            return ""

