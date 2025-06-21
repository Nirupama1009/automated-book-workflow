import chromadb
from chromadb.config import Settings

# Initialize client
client = chromadb.Client(Settings(
    persist_directory="./chroma_store",
    anonymized_telemetry=False
))

# Load collection
collection = client.get_or_create_collection("book_versions")

def search_chapter(query: str):
    results = collection.query(
        query_texts=[query],
        n_results=1
    )

    print("\n🔍 Search Query:", query)
    print("🎯 Best Match Found:\n")
    print(results['documents'][0][0])

if __name__ == "__main__":
    user_query = input("Enter a search query related to the chapter content: ")
    search_chapter(user_query)
