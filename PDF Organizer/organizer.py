
import os
import shutil
from PyPDF2 import PdfReader

SOURCE_DIR = "pdfs"
DEST_DIR = "organized_pdfs"

def get_author(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        author = reader.metadata.author
        return author.strip().replace(" ", "_") if author else "Unknown_Author"
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return "Unknown_Author"

def organize_by_author():
    os.makedirs(DEST_DIR, exist_ok=True)
    
    for filename in os.listdir(SOURCE_DIR):
        if filename.lower().endswith(".pdf"):
            file_path = os.path.join(SOURCE_DIR, filename)
            author = get_author(file_path)

            author_dir = os.path.join(DEST_DIR, author)
            os.makedirs(author_dir, exist_ok=True)

            dest_path = os.path.join(author_dir, filename)
            shutil.copy2(file_path, dest_path)
            print(f"Moved {filename} to {author_dir}")

if __name__ == "__main__":
    organize_by_author()
