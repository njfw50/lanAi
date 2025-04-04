import os
import sys
import PyPDF2
from lanai_core import run_lanai_core
from lanAi_storage import init_db, insert_knowledge, get_all_knowledge

DATA_DIR = "data"
PDF_DIR = "pdfs"

def show_welcome_message():
    print("\n🧠 Welcome to LanAi!")
    print("""
LanAI is LibertyM's smart assistant.
The name comes from LAN (Local Area Network) + AI (Artificial Intelligence).
Interestingly, “lanai” is also a Hawaiian word that means a covered veranda or open patio —
a space between the technical and the practical — just like me, your assistant.
""")

def call_ai():
    user_question = input("🤖 Ask LanAI something: ").strip()
    if not user_question:
        print("⚠️ Empty prompt.")
        return

    context = get_all_knowledge()
    full_prompt = f"""Here is some internal company information:\n{context}\n\nQuestion: {user_question}"""

    print("\n🧠 LanAI's response:\n" + "-" * 40)
    print(run_lanai_core(full_prompt))
    print("-" * 40)

def main_menu():
    options = {
        "1": extract_text,
        "2": insert_manual,
        "3": search_info,
        "4": call_ai,
        "0": exit_lanai
    }

    while True:
        print("\n📋 MAIN MENU")
        print("1. Extract text from PDFs")
        print("2. Insert manual information")
        print("3. Search for information")
        print("4. Ask something to LanAI")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        action = options.get(choice)

        if action:
            try:
                action()
            except Exception as e:
                print(f"\n❌ An error occurred while executing the option: {e}")
        else:
            print("❌ Invalid option. Please try again.")

def extract_text():
    if not os.path.exists(PDF_DIR):
        print(f"📂 Folder '{PDF_DIR}' not found.")
        return

    for filename in os.listdir(PDF_DIR):
        if filename.lower().endswith(".pdf"):
            file_path = os.path.join(PDF_DIR, filename)
            print(f"\n📄 Reading: {filename}")
            try:
                with open(file_path, "rb") as f:
                    reader = PyPDF2.PdfReader(f)
                    for i, page in enumerate(reader.pages):
                        text = page.extract_text()
                        if text:
                            print(f"\nPage {i + 1}:\n{text}")
                            insert_knowledge(f"PDF: {filename}", text)
            except Exception as e:
                print(f"⚠️ Could not read {filename}: {e}")

def insert_manual():
    entry = input("📝 Type the information to insert: ").strip()
    if not entry:
        print("⚠️ Empty entry. Aborting.")
        return

    insert_knowledge("Manual", entry)
    print("✅ Entry saved to database.")

def search_info():
    keyword = input("🔍 Enter keyword to search: ").strip().lower()
    if not keyword:
        print("⚠️ Empty keyword. Aborting.")
        return

    all_data = get_all_knowledge()
    matches = [line for line in all_data.split('\n') if keyword in line.lower()]

    if matches:
        print(f"\n🔎 Found {len(matches)} matching lines:\n")
        for m in matches:
            print(f"👉 {m}")
    else:
        print("🔕 No matching information found.")

def exit_lanai():
    print("\n🛑 Shutting down LanAi... See you next time!")
    sys.exit(0)

if __name__ == "__main__":
    init_db()
    show_welcome_message()
    main_menu()
