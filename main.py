import os
from extractors import extract_name, extract_email, extract_phone, extract_skills
import re

def natural_sort_key(text):
    return [int(s) if s.isdigit() else s.lower() for s in re.split(r'(\d+)', text)]

folder_path = 'resumes'
files = sorted(os.listdir(folder_path), key=natural_sort_key)

for file_name in files:
    if file_name.endswith('.txt'):
        with open(os.path.join(folder_path, file_name), 'r', encoding='utf-8') as file:
            content = file.read()

        name = extract_name(content)
        email = extract_email(content)
        phone = extract_phone(content)
        skills = extract_skills(content)

        print(f'📄 Resume: {file_name}')
        print(f'Name: {name}')
        print(f'Email: {email}')
        print(f'Phone: {phone}')
        print(f'Skills: {skills}\n')
