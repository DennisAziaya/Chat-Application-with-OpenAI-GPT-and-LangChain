# Import necessary modules
import langchain
from decouple import config
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores.chroma import Chroma

# Import custom module
from redundant_filter_retriever import RedundantFilterRetriever

# Enable debugging for langchain
langchain.debug = True

# Initialize ChatOpenAI instance with the OpenAI API key from configuration
chat = ChatOpenAI(openai_api_key=config("OPENAI_API_KEY"))

# Initialize OpenAIEmbeddings instance with the OpenAI API key from configuration
embeddings = OpenAIEmbeddings(openai_api_key=config("OPENAI_API_KEY"))

# Initialize Chroma vector store with specified parameters
db = Chroma(
    embedding_function=embeddings,
    persist_directory="emb"
)

# Initialize RedundantFilterRetriever with embeddings and Chroma vector store
retriever = RedundantFilterRetriever(
    embeddings=embeddings,
    chroma=db
)

# Initialize RetrievalQA chain with ChatOpenAI, RedundantFilterRetriever, and specified chain type
chain = RetrievalQA.from_chain_type(
    llm=chat,
    retriever=retriever,
    chain_type="stuff"
)

# Run the chain with a sample input and print the response
response = chain.run("What does the bible says about love")

print(response)
