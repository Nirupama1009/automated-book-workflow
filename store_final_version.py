from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer
import os

# Initialize ChromaDB
client = PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="chapters")

# Load final edited chapter
file_path = "final_chapter.txt"
if not os.path.exists(file_path):
    print(f"❌ File '{file_path}' not found.")
    exit(1)

with open(file_path, "r", encoding="utf-8") as f:
    final_text = f.read()

# Generate embedding using SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
embedding = model.encode(final_text)

# Store in ChromaDB
collection.add(
    documents=[final_text],
    embeddings=[embedding.tolist()],
    ids=["chapter_1_final"]
)

print("✅ Final version stored in ChromaDB under ID: chapter_1_final")
