# 🔎 Smart PDF Keyword Highlighter

A simple and interactive **Streamlit app** that searches for keywords inside multiple PDF files, highlights them in yellow, and generates new annotated PDFs automatically.

---

## 🚀 Features

- 🔍 Search keywords inside PDF files
- 📂 Automatically reads all PDFs from a folder
- 🟡 Highlights matched words in yellow
- 📄 Generates new PDF files with highlights
- ⚡ Simple web interface using Streamlit
- 🔤 Case-insensitive keyword search
- 📊 Displays which files contain the searched words

---

## 🧠 How it works

1. User types one or more keywords
2. App reads all PDFs inside the `pdf/` folder
3. Each PDF is scanned page by page
4. Matching words are searched and highlighted
5. A new PDF is saved with annotations
6. Results are displayed in the interface

---

## 📁 Project Structure


Smart-PDF-Keyword-Highlighter/
│
├── code.py
├── pdf/
│ ├── example1.pdf
│ ├── example2.pdf
│
├── resultado_example1.pdf
└── README.md


---

Type keywords separated by commas:

contract, payment, agreement
Click Buscar
View results in the interface
Download or open generated highlighted PDFs
📌 Example

Input:

contract, agreement

Output:

PDFs with highlighted words 🟡
List of files where keywords were found
