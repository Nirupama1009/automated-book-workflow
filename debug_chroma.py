import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings(
    persist_directory="./chroma_store",
    anonymized_telemetry=False
))

collection = client.get_or_create_collection("book_versions")
results = collection.get()

print(f"\n📦 Total documents stored: {len(results['documents'])}")
if results['documents']:
    print("✅ First document preview:\n")
    print(results['documents'][0][:300])  # Show first 300 characters
else:
    print("⚠️ No documents found in ChromaDB.")
