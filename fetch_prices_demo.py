"""
Demo script for collecting latest stock prices and outputting CSV data with a custom delimiter.
"""

from c64.helpers import invoke_llm, set_system_prompt_for_llm, collect_data_from_web
import asyncio
import csv

set_system_prompt_for_llm("You are specialized in returning data you got from the user in the requested format. Make sure you reply with the string representation of the formated data.")

async def main():
    rows = []
    rows.append(["Ticker", "Price"])
    for ticker in ["AAPL", "GOOGL", "TSLA"]:
        ticker_price = await collect_data_from_web(
                f"What is the latest price of {ticker}?"
                f"Reply only with the price in dollars without any symbols other than the decimal point."
                f"Make sure you get latest data from Yahoo Finance. Do not include any markup."
            )
        rows.append([ticker, ticker_price])

    output = invoke_llm(
        prompt=(
            f"Here is the data I collected from the web: {rows}."
            f"I want it in the CSV format with a dollar sign set as the delimiter. Do not include any markup."
        ),
        model="gpt-4o",
        temperature=0.7
    )

    print(output)

    with open("output.csv", "w") as f:
        f.write(output)

    with open("output1.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

asyncio.run(main())