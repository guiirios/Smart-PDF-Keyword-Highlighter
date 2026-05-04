# 🔎 PDF Keyword Highlighter (Python + Streamlit)

A simple **Python-based Streamlit application** that searches for keywords inside multiple PDF files, highlights the matches in yellow, and generates new annotated PDFs automatically.

---



## 🐍 Built With Python

This project is fully developed using **Python**, leveraging powerful libraries for automation and document processing:

- 🐍 Python (core language)
- 📄 PyMuPDF (fitz) for PDF manipulation
- 🌐 Streamlit for web interface
- 📁 OS module for file handling

---

## 🚀 Features

- 🔍 Search keywords inside multiple PDF files
- 📂 Automatically reads all PDFs from a folder (`pdf/`)
- 🟡 Highlights all matched words in yellow
- 📄 Generates new PDFs with highlighted text
- ⚡ Simple web interface using Streamlit
- 🔤 Case-insensitive keyword search
- 📊 Shows which files contain the searched words

---

## 🧠 How it works

1. User enters one or more keywords (comma-separated)
2. Python reads all PDFs inside the `pdf/` folder
3. Each PDF is opened and processed page by page
4. Text is extracted and searched for matches
5. Matching words are highlighted using PyMuPDF
6. A new PDF is saved with the prefix `resultado_`
7. Results are displayed in the Streamlit interface

---


## 📁 Project Structure

project/
│
├── app.py
├── pdf/
│ ├── file1.pdf
│ ├── file2.pdf
│
├── resultado_file1.pdf
└── README.md

# 🚧 Project Status

## 🟡 This project is ONGOING

This project is currently under development and continuous improvement.

New features, optimizations, and UI enhancements are being added regularly.


