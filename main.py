# Importing necessary modules
from decouple import config  # For reading configuration variables
from langchain.text_splitter import CharacterTextSplitter  # Text splitting utility
from langchain_community.document_loaders import TextLoader  # Text loading utility
from langchain.vectorstores.chroma import Chroma  # Vector store for document embeddings
from langchain_community.embeddings import OpenAIEmbeddings  # Embeddings utility

# Creating a CharacterTextSplitter instance with specific configuration
text_splitter = CharacterTextSplitter(
    separator="\n",  # Set the separator to newline character
    chunk_size=200,  # Set the maximum size of each chunk to 200 characters
    chunk_overlap=0  # Set the overlap between chunks to 0 characters
)

# Creating a TextLoader instance for the file "quotes.txt"
loader = TextLoader("quotes.txt")

# Loading and splitting text from the file using the configured text splitter
docs = loader.load_and_split(text_splitter=text_splitter)

# Initializing OpenAIEmbeddings with API key from environment variable
embeddings = OpenAIEmbeddings(openai_api_key=config("OPENAI_API_KEY"))

# Creating a Chroma vector store from the documents with embeddings
# Persisting the vectors in the "emb" directory
db = Chroma.from_documents(
    docs,
    embedding=embeddings,
    persist_directory="emb"
)

# Performing similarity search with a query on the vector store
response = db.similarity_search_with_score("what does God say about love")

# Printing the results of the similarity search
for result in response:
    print("\n")
    print(result[1])  # Printing the similarity score
    print(result[0].page_content)  # Printing the content of the matching document
