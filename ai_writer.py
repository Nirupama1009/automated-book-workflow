from bs4 import BeautifulSoup

def extract_text_from_html(file_path):
    """Extract plain text from the saved HTML file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        return soup.get_text()

def ai_spin(text):
    """Simulated AI Writer – spins the chapter into a new version."""
    # You can later replace this with actual OpenAI/Gemini logic
    return f"🔁 [AI Writer Output]:\n{text[:500]}...\n\n(This is a preview of spun text. In production, this would be rewritten by GPT.)"

def main():
    raw_text = extract_text_from_html("chapter.html")
    spun_text = ai_spin(raw_text)

    with open("spun_chapter.txt", "w", encoding="utf-8") as f:
        f.write(spun_text)

    print("[✓] AI-spun version saved to 'spun_chapter.txt'.")

if __name__ == "__main__":
    main()
