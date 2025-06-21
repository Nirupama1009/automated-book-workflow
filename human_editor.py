def load_reviewed_text(file_path="reviewed_chapter.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def save_final_version(text, file_path="final_chapter.txt"):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)

def main():
    reviewed_text = load_reviewed_text()
    
    print("---- START OF REVIEWED TEXT ----\n")
    print(reviewed_text[:1000])  # Show only the first 1000 characters
    print("\n---- END OF PREVIEW ----\n")
    
    print("📝 Please open 'reviewed_chapter.txt' in any text editor, make your changes, and save it.")
    input("Once you've edited and saved, press ENTER to continue...")

    with open("reviewed_chapter.txt", "r", encoding="utf-8") as f:
        edited_text = f.read()

    save_final_version(edited_text)
    print("[✓] Human-edited final version saved to 'final_chapter.txt'.")

if __name__ == "__main__":
    main()
