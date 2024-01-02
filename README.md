# Chat Application with OpenAI GPT and LangChain

This repository contains a Python script for an interactive chat application powered by OpenAI's GPT model. The script utilizes the langchain library to manage conversation memory, construct prompts, and interact with the language model.

## Features

- **OpenAI GPT-3 Integration:** The chat application leverages the ChatOpenAI model from langchain for natural language processing.
  
- **Conversation Memory Management:** The script utilizes ConversationSummaryMemory to manage conversation history, facilitating more context-aware interactions.

- **Prompt Template Construction:** The ChatPromptTemplate class is employed to structure prompts, including placeholders for previous messages and templates for user input.

- **Continuous Interaction:** The script includes a continuous loop for interactive chat, where users can input messages and receive responses from the language model.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/DennisAziaya/Chat-Application-with-OpenAI-GPT-and-LangChain.git

2. Install requirement:
   ```bash
   pip install -r requirements.txt

3. Run the chat application:
   ```bash
   python main.py
