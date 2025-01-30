from c64.helpers import invoke_llm, set_system_prompt_for_llm, collect_data_from_web
import asyncio

set_system_prompt_for_llm("You are specialized in returning data you got from the user in the requested format. Make sure you reply with the string representation of the formated data.")

async def main():
    data = {}
    for ticker in ["AAPL", "GOOGL", "TSLA"]:
        data[ticker] = await collect_data_from_web(f"What is the latest price of {ticker}? Reply only with the price in dollars without any symbols other than the decimal point. Make sure you get latest data from Yahoo Finance. Do not include any markup.")

    output = invoke_llm(
        prompt=f"Here is the data I collected from the web: {data}. I want it in the CSV format with a dollar sign set as the delimiter.",
        model="gpt-4o",
        temperature=0.7
    )

    print(data)
    print(output)

asyncio.run(main())