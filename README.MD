# Resume Parser (Rule-Based)

This is a simple rule-based resume parser built using Python. It extracts key information such as:

- Name
- Email
- Phone Number
- Skills

The project processes plain text resumes (`.txt` files) and prints the extracted details for each one.

---

##  Project Structure

resume-parser/
│
├── extractors.py → Reusable functions for extracting name, email, phone, and skills
├── main.py → Main script that loads and processes all resumes
├── resumes/ → Folder containing sample .txt resume files
├── README.md → Project documentation (this file)


---

## Features

- Regex-based name, email, and phone extraction
- Skill extraction using:
  - Structured `[skill1, skill2]` list parsing
  - Fallback keyword-matching from a predefined set
- Natural sorting of resume files (e.g., resume2.txt comes before resume10.txt)
- Modular structure for easy maintenance

---

##  How to Run

1. Clone the repository or download the folder:

git clone https://github.com/your-username/resume-parser.git
cd resume-parser
Place your .txt resumes inside the resumes/ folder.

Run the main script:

python main.py
You’ll see output like:

Resume: resume1.txt
Name: Ramesh Singh
Email: ramesh.singh23@gmail.com
Phone: 9876543210
Skills: ['python', 'excel']

Resume: resume2.txt
Name: Sneha Kapoor
Email: sneha.kapoor@yahoo.com
Phone: 9123456789
Skills: ['sql']



 Requirements
No external libraries are needed except the standard Python library. Make sure you're using Python 3.6+.

 Example Skill Keywords Used

python

java

excel

sql

machine learning

data analysis

react

html

css

javascript

nlp

coding

---

## Author

Made with  by **Trashu**  
`NLP Freelancer & Engineer`


