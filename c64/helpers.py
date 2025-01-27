from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv

import logging

logging.getLogger("browser_use").setLevel(logging.ERROR)

load_dotenv()

system_prompt_for_llm = None

def set_system_prompt_for_llm(system_prompt: str) -> None:
    """
    Set the system prompt for the LLM model.
    """
    global system_prompt_for_llm
    system_prompt_for_llm = system_prompt

def invoke_llm(
        prompt: str,
        model: str = "gpt-4o",
        temperature: float = 0.7,
    ) -> str:

    """
    Invoke the LLM model to generate text.

    Parameters:
    prompt (str): The prompt to send to the LLM.
    model (str): The model to use for the LLM. Default is "gpt-4o".
    temperature (float): The temperature setting for the LLM. Default is 0.7.

    Returns:
    str: The generated text from the LLM.
    """
    llm = ChatOpenAI(
        model=model,
        temperature=temperature
    )

    messages = []

    if system_prompt_for_llm:
        messages.append(("system", system_prompt_for_llm))
    
    messages.append(("user", prompt))

    return llm.invoke(messages).content

async def collect_data_from_web(task: str) -> str:
    """
    Collect data from the web for a given task.

    Parameters:
    task (str): The task to collect data for.

    Returns:
    str: The collected data from the web.
    """
    
    agent = Agent(
        task=task,
        llm=ChatOpenAI(model="gpt-4o")
    )

    result = await agent.run()
    
    last_action_result = result.final_result()

    return last_action_result
    