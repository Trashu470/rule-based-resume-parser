import re
import ast

def extract_name(text):
    match = re.search(r'Name\s*[:\-]\s*(.+)', text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    name_match = re.findall(r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b', text)
    if name_match:
        return name_match[0] 

    return None

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    return match.group(0) if match else None

def extract_phone(text):
    match = re.search(r'\b(?:\+91[-\s]?)?[6-9]\d{9}\b', text)
    return match.group(0) if match else None

def extract_skills(text):
    pattern = r'(Skills|Expertise|Technical Skills|Core Competencies)\s*[:\-]\s*(\[.*?\])'
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        try:
            skill_list = ast.literal_eval(match.group(2))
            return [skill.strip().lower() for skill in skill_list if isinstance(skill, str)]
        except Exception:
            pass

    skill_keywords = ['python', 'java', 'excel', 'sql', 'machine learning', 'data analysis', 'react', 'html', 'coding', 'nlp', 'css', 'javascript']

    found_skills = []
    for skill in skill_keywords:
        if re.search(r'\b' + re.escape(skill) + r'\b', text, re.IGNORECASE):
            found_skills.append(skill.lower())

    return found_skills


