"""
Demo script for collecting the latest stock news and outputting results in a different format.
"""

import json
import asyncio
from c64.helpers import collect_data_from_web

async def fetch_news_data(ticker: str) -> dict:
    prompt = (
        f'Give me important news about {ticker}. '
        f'Reply with valid JSON containing these attributes: '
        f'{{ "ticker": "{ticker}", "headline": "...", "summary": "..." }}'
    )
    response_text = await collect_data_from_web(prompt)

    return json.loads(response_text)

async def main():
    tickers = ["AAPL", "GOOGL", "TSLA"]
    all_news = []

    for ticker in tickers:
        news_data = await fetch_news_data(ticker)
        all_news.append(news_data)

    print(all_news)

if __name__ == "__main__":
    asyncio.run(main())