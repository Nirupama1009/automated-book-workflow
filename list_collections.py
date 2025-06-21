import chromadb

# Connect to ChromaDB storage
client = chromadb.PersistentClient(path="chroma_db")

# Show what collections exist
collections = client.list_collections()

if not collections:
    print("❌ No collections found.")
else:
    print("✅ Found these collections:")
    for c in collections:
        print("📦", c.name)
