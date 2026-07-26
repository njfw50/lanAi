# lanAi - Your Local and Intelligent AI Assistant

**lanAi** is a generative AI assistant built in Python, designed to run locally. It can learn from your documents (PDFs) and other data sources to provide intelligent, contextualized answers, ensuring full privacy and control over your information.

The name **lanAi** comes from the combination of **LAN** (Local Area Network) and **AI** (Artificial Intelligence), reflecting its ability to operate in a local environment. Interestingly, "lanai" is also a Hawaiian word that means a covered veranda or open courtyard - a space between the technical and the practical - just like this assistant.

---

## ✨ Main Features

- **Local Learning:** Extracts text from PDF files in a local directory to build its knowledge base.
- **Expandable Knowledge Base:** Allows manual insertion of information, in addition to automatic learning from documents.
- **Command Line Interface (CLI):** An interactive and easy-to-use menu to manage the knowledge base and interact with the AI.
- **Privacy First:** Because it runs locally, your data never leaves your computer.
- **Modular and Extensible:** The code is organized into modules, making it easy to add new features and data sources.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- The libraries listed in the `requirements.txt` file

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/njfw50/lanAi.git
   cd lanAi
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Put the PDF files you want lanAi to learn from into the `pdfs` folder.

### Running

To start the assistant, run the main script:

```bash
python lanAi.py
```

You will be greeted with a welcome message and the main menu, where you can choose between extracting text from PDFs, inserting information manually, searching the knowledge base, or chatting with the AI.

---

## 🔧 Project Structure

- `lanAi.py`: The main entry point of the application, containing the menu and the user interaction logic.
- `lanai_core.py`: The assistant's "brain", responsible for processing questions and generating answers using the knowledge base.
- `lanAi_storage.py`: Manages the SQLite database where all knowledge is stored.
- `pdfs/`: Directory where you should place your PDF files for learning.

---

## 🤝 Contributions

Contributions are welcome! Feel free to open an *issue* to report bugs or suggest new features. If you want to contribute code, please open a *pull request*.