from sentence_transformers import SentenceTransformer
import chromadb

# Load the model
model = SentenceTransformer("all-MiniLM-L6-v2")

# ✅ NEW Chroma client (persistent mode)
client = chromadb.PersistentClient(path="chroma_db")

# Connect to existing collection
collection = client.get_collection("chapters")  # ✅ correct

# Get a user query
query = input("🔎 Enter your question or search query: ")

# Convert query to embedding
query_embedding = model.encode(query).tolist()

# Perform semantic search
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

# Display top matches
print("\n✅ Top Matches:\n")
for i, doc in enumerate(results["documents"][0]):
    print(f"{i + 1}. {doc}\n")
