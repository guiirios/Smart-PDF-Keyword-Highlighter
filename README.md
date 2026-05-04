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


---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/your-username/pdf-keyword-highlighter.git
cd pdf-keyword-highlighter
2. Install dependencies
pip install streamlit pymupdf
▶️ How to run
streamlit run app.py

Then open in your browser:

http://localhost:8501
🌐 Why Streamlit uses port 8501

When you run:

streamlit run app.py

It opens:

http://localhost:8501
🧠 What is 8501?

👉 8501 is the default port used by Streamlit.

A port is like a “door” your application uses to run on your computer.

💡 Simple explanation
Computer = building
Port = door
localhost = your own machine

So:

localhost:8501 = your app running locally on your computer
🔧 Can you change it?

Yes:

streamlit run app.py --server.port 8502

Then:

http://localhost:8502
💡 Usage
Open the app
Type keywords separated by commas:
contract, agreement, payment
Click Buscar
The app will:
Scan all PDFs
Highlight matches
Show results
Generate new PDFs
📌 Example

Input:

contract, payment

Output:

PDFs with highlighted words 🟡
List of files where words were found
New files saved as:
resultado_filename.pdf
🧠 Use cases
Document review automation
Legal document scanning
Academic PDF research
Business contract analysis
Text search across multiple documents
🚀 Future improvements
📤 Upload PDFs via interface
📄 Show page number of matches
📦 Download results as ZIP
🎨 Improve UI design
🔎 Phrase-based search
👨‍💻 Author

Built as a learning project focused on:

Automation
PDF processing
Python logic
Streamlit web apps
