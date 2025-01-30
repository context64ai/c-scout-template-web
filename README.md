# c-scout-template-web

A sample AI Agent for autonomous navigation and data gathering from websites. 🕵️‍♂️

## Requirements

- Python ≥ 3.13, preferably in a virtual environment
- [uv](https://github.com/astral-sh/uv), a package and project manager

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/c-scout-template-web.git
   cd c-scout-template-web
   ```

2. Install the required dependencies using `uv`:

   ```bash
   uv install
   ```

3. Copy `example.env` to `.env` and edit the encironment variables (e.g., `OPENAI_API_KEY`):

   ```bash
   cp .example.env .env
   ```

## Usage

### Fetching stock prices

To run the demo script for fetching the latest stock prices and outputting CSV data with a custom delimiter:

```bash
uv run fetch_prices_demo.py
```

### Fetching stock news

To run the demo script for fetching the latest stock news and outputting results in JSON format:

```bash
uv run fetch_news_demo.py
```

Enjoy exploring data on the web!
