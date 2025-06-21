from transformers import pipeline

# Load chapter text
with open("chapter1.txt", "r", encoding="utf-8") as file:
    context = file.read()

# Load Hugging Face's QA model
qa_pipeline = pipeline("question-answering")

# Ask user for a question
question = input("🤖 Ask a question about the chapter: ")

# Get the answer from the model
result = qa_pipeline(question=question, context=context)

# Print the answer
print("💡 Answer:", result["answer"])
