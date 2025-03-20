import PyPDF2
import pdfplumber
import spacy
from spacy.matcher import PhraseMatcher
import datafile
import re

class resume_helper:

    def __init__(self,path):
        self.path = path
        self.nlp = spacy.load("en_core_web_sm")
        self.matcher = PhraseMatcher(self.nlp.vocab, attr="LOWER")
        # self.text = self.extract_text()
        self.text = "Experienced in Python, TensorFlow, AWS, and Docker for machine learning workflows. MBA from Havard"
        self.doc = self.nlp(self.text)

        self.educations_found = self.matcher_func("education", datafile.education)
        self.skills_found = self.matcher_func("skills", datafile.skills)
        self.jobs_found = self.matcher_func("job_titles", datafile.job_titles,
                                            {"work_section": datafile.work_section, "other_sections": datafile.other_sections})

        print("Skills found:", self.skills_found)
        print("Education found:", self.educations_found)
        print("Jobs found:", self.jobs_found)

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

    def matcher_func(self, match_name: str, pattern_array, sections: dict = None):

        '''
        Later
        '''
        patterns = [self.nlp.make_doc(pattern) for pattern in pattern_array]

        # if match_name in self.matcher:
        #     self.matcher.remove(match_name)

        self.matcher.add(match_name, None, *patterns)

        if not sections:
            patterns_found = self.extract_pattern(match_name=match_name)
        else:
            for match, pat in sections.items():
                patterns = [self.nlp.make_doc(pattern) for pattern in pat]
                self.matcher.add(match, None, *patterns)

            patterns_found = self.extract_pattern(match_name=match_name, whole_doc=False)

        return patterns_found

    def extract_pattern(self, match_name, matches=None, whole_doc=True):

        '''
        Later
        '''


        if not matches:
            matches = self.matcher(self.doc)

        if whole_doc:
            found_patterns = set()
            for match_id, start, end in matches:
                string_id = self.nlp.vocab.strings[match_id]
                if string_id == match_name:
                    span = self.doc[start:end]
                    found_patterns.add(span.text)
            return list(found_patterns)


        # This grabs a relevant section such as work experience section, then recursively finds the needed pattern
        else:
            start_index = None
            end_index = None
            for match_id, start, end in matches:
                string_id = self.nlp.vocab.strings[match_id]
                span = self.doc[start:end]

                if string_id == "work_section" and start_index is None:
                    start = span.end_char  # Where the section starts (after the header)
                    start_index = end

                if string_id == "other_sections" and start_index is not None and span.start_char > start:
                    end_index = start
                    break

        if start_index and end_index:
            return self.extract_pattern(match_name=match_name, matches=self.matcher(self.doc[start_index:end_index]))
        elif start_index:
            return self.extract_pattern(match_name=match_name, matches=self.matcher(self.doc[start_index:]))



if __name__ == "__main__":
    path = "pdf_path"
    parser = resume_helper(path)