# Import necessary modules and libraries
from decouple import config
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)

from langchain.agents import OpenAIFunctionsAgent, AgentExecutor

# Import a specific SQL query tool
from tools.sql import run_query_tool

# Initialize the ChatOpenAI instance with the OpenAI API key from the configuration
chat = ChatOpenAI(openai_api_key=config("OPENAI_API_KEY"))

# Define a list of tools, in this case, only the SQL query tool is included
tools = [run_query_tool]

# Define a template for the conversation prompt with a human message and a placeholder for the agent's scratchpad
prompt = ChatPromptTemplate(
    messages=[
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

# Initialize the OpenAIFunctionsAgent with the ChatOpenAI instance, prompt template, and tools
agent = OpenAIFunctionsAgent(
    llm=chat,
    prompt=prompt,
    tools=tools,
)

# Initialize an AgentExecutor with the OpenAIFunctionsAgent, enabling verbose mode and providing the list of tools
agent_executor = AgentExecutor(agent=agent, verbose=True, tools=tools)

# Run the agent with a specific prompt
agent_executor.run("What is the total number of users in the database?")

