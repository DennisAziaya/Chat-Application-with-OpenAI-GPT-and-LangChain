# Importing necessary classes and functions from langchain and decouple modules
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import MessagesPlaceholder, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.memory import ConversationSummaryMemory, ConversationBufferMemory, FileChatMessageHistory
from decouple import config

# Initializing the ChatOpenAI Model with the OpenAI API key obtained from environment variables
chat = ChatOpenAI(
    api_key=config('openai_key'),
    verbose=True  # Enable verbose logging
)

# Initializing a ConversationSummaryMemory to manage conversation memory
memory = ConversationSummaryMemory(
    memory_key="messages",
    return_messages=True,
    llm=chat  # Linking the language model to the memory
)

# Setting up the Chat Prompt Template for constructing prompts
prompt = ChatPromptTemplate(
    input_variables=["content", "messages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),  # Placeholder for previous messages
        HumanMessagePromptTemplate.from_template("{content}")  # Template for user's input
    ]
)

# Initializes a language model chain with the OpenAI model, prompt template, and memory
chain = LLMChain(
    llm=chat,
    prompt=prompt,
    memory=memory,
    verbose=True  # Enable verbose logging for the chain
)

# Continuous loop for interactive chat
while True:
    # Get user input
    content = input(">>> ")
    
    # Feed the input to the language model chain and get the response
    response = chain({"content": content})
    
    # Print the response text
    print(response['text'])
