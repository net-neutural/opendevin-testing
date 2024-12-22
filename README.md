# Hacker News Top Story Extractor

This repository contains a Python web app that displays the top stories from Hacker News, including the title, link, points, author, and number of comments.

## Usage

### Web App

1. **Install dependencies:**
   ```bash
   pip install flask requests beautifulsoup4
   ```

2. **Run the app:**
   ```bash
   python app.py
   ```

3. **View in browser:**
   Open your web browser and go to `http://127.0.0.1:5000` to view the top stories.

### Text Chunking

1. **Install dependencies:**
   ```bash
   pip install tiktoken
   ```

2. **Chunk the text file:**
   ```bash
   python chunk_text.py
   ```

3. **Output:**
   The script will read `folder/file.txt`, split it into chunks of 2048 tokens, and save them as `chunk1.txt`, `chunk2.txt`, etc., in the `folder/` directory.

## Features

- Displays the top 5 stories from Hacker News.
- Shows the title, link, points, author, and number of comments for each story.

## Contributing

Contributions to improve the script are welcome. Please open an issue or pull request with your proposed changes.
