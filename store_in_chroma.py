import chromadb
from chromadb.config import Settings

# Setup ChromaDB client
client = chromadb.Client(Settings(
    persist_directory="./chroma_store",  # Stores data here
    anonymized_telemetry=False
))

# Create or get collection
collection = client.get_or_create_collection("book_versions")

def store_final_version():
    with open("final_chapter.txt", "r", encoding="utf-8") as f:
        final_text = f.read()

    # Add to ChromaDB
    collection.add(
        documents=[final_text],
        metadatas=[{"version": "v1", "status": "final"}],
        ids=["chapter_1"]
    )

    print("[✓] Final chapter stored in ChromaDB under collection 'book_versions'.")

if __name__ == "__main__":
    store_final_version()
