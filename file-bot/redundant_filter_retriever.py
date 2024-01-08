# Import necessary modules from langchain
from langchain.vectorstores import Chroma
from langchain.embeddings.base import Embeddings
from langchain.schema import BaseRetriever


# Define a custom retriever class that inherits from BaseRetriever
class RedundantFilterRetriever(BaseRetriever):
    # Define class attributes for embeddings and Chroma vector store
    embeddings: Embeddings
    chroma: Chroma

    # Define a method to get relevant documents based on a query
    def get_relevant_documents(self, query):
        # Embed the query using the specified embeddings
        emb = self.embeddings.embed_query(query)

        # Use Chroma vector store for max marginal relevance search by vector
        return self.chroma.max_marginal_relevance_search_by_vector(
            embedding=emb,
            lambda_mult=0.8
        )

    # Define an asynchronous version of the method (empty implementation for now)
    async def aget_relevant_documents(self):
        return []
