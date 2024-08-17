# Chatbot with PDF and Web Data Integration

![Chatbot Banner](./assets/chatbot-banner.png)

## Overview

This project is a versatile chatbot powered by OpenAI that can read and comprehend text from PDF documents and data scraped from web pages. The chatbot answers user queries intelligently based on the extracted content, making it a powerful tool for automating information retrieval and decision-making processes.

## Features

- **PDF Text Extraction**: Processes and extracts text from PDF files for querying.
- **Web Scraping Integration**: Scrapes and structures data from web pages.
- **Intelligent Query Handling**: Leverages OpenAI to provide context-aware responses.
- **Customizable Prompts**: Tailor the chatbot's responses based on specific needs.
- **Easy Integration**: Can be integrated into web applications or hosted independently.

## Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key
- Libraries:
  - `openai`
  - `PyPDF2` or `pdfminer.six`
  - `beautifulsoup4` or `scrapy`
  - `requests` (optional, for web scraping)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/chatbot-pdf-web.git
   cd chatbot-pdf-web
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up OpenAI API Key**:
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key:
     ```plaintext
     OPENAI_API_KEY=your-openai-api-key
     ```

### Usage

#### PDF Processing

1. Place your PDF files in the `pdfs/` directory.
2. Run the script to extract text and prepare it for querying:
   ```bash
   python process_pdfs.py
   ```

#### Web Scraping

1. Define your scraping logic in `scrape_data.py`.
2. Run the scraper to collect and structure data:
   ```bash
   python scrape_data.py
   ```

#### Ask Questions

1. Start the chatbot:
   ```bash
   python chatbot.py
   ```
2. Interact with the chatbot by asking questions related to the processed PDFs and scraped web data.

### Example

```bash
User: What is the main topic discussed in the document?
Chatbot: The main topic of the document is [Topic], which covers various aspects including [Details].
```

## Project Structure

```plaintext
├── assets/
│   └── chatbot-banner.png      # Optional: Banner for the README
├── pdfs/                       # Directory for PDF files
├── scraped_data/               # Directory for storing scraped data
├── process_pdfs.py             # Script for processing PDFs
├── scrape_data.py              # Script for web scraping
├── chatbot.py                  # Main chatbot script
├── requirements.txt            # Python dependencies
└── README.md                   # Project README file
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
