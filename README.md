# Automated Book Publication Workflow 📚🤖

This project automates the workflow of creating book chapters using AI tools. It includes scraping content, spinning/rephrasing it using an LLM, reviewing for quality, and storing results with versioning.

## Features
- ✅ Web scraping with Playwright
- ✅ AI-based content spinning (LLM)
- ✅ Human-in-the-loop content review
- ✅ Version control using ChromaDB
- ✅ Screenshot proof of working app

## Tech Stack
- Python 🐍
- Playwright for scraping 🌐
- ChromaDB for vector storage 💾
- OpenAI API (or LLM of your choice) 🧠

## How to Run
1. Clone the repo
2. Set up a virtual environment and install dependencies
3. Run `scraper.py` to scrape content
4. Run `ai_writer.py` to rewrite content using LLM
5. Manually review content in `ai_reviewer.py`

## Output
- `spun_chapter.txt` – contains spun content
- `chapter.html` – raw scraped data
- `screenshot.png` – screenshot of working app

## Author
- Nirupama @ Softnerve Technology Pvt Ltd
