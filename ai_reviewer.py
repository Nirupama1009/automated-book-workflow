def review_text(text):
    
    
    lines = text.splitlines()
    reviewed = []

    for line in lines:
        if line.strip():
            reviewed.append(line)
            reviewed.append(f"[AI Review Note]: Consider clarifying or enriching this paragraph.\n")
        else:
            reviewed.append("\n")

    return "\n".join(reviewed)

def main():
    with open("spun_chapter.txt", "r", encoding="utf-8") as f:
        spun_text = f.read()

    reviewed_text = review_text(spun_text)

    with open("reviewed_chapter.txt", "w", encoding="utf-8") as f:
        f.write(reviewed_text)

    print("[✓] Reviewed version saved to 'reviewed_chapter.txt'.")

if __name__ == "__main__":
    main()
