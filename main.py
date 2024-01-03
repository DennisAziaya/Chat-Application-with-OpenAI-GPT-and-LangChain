# Importing necessary modules
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader

# Creating a CharacterTextSplitter instance with specific configuration
text_splitter = CharacterTextSplitter(
    separator="\n",  # Set the separator to newline character
    chunk_size=200,  # Set the maximum size of each chunk to 200 characters
    chunk_overlap=0  # Set the overlap between chunks to 0 characters
)

# Creating a TextLoader instance for the file "quotes.txt"
loader = TextLoader("quotes.txt")

# Loading and splitting text from the file using the configured text splitter
docs = loader.load_and_split()

# Iterating through each document (presumably each chunk of text)
for doc in docs:
    # Printing the content of each chunk
    print(doc.page_content)

    # Printing an extra newline to visually separate chunks
    print("\n")
