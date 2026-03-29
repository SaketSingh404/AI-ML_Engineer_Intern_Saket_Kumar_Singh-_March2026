from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

# 1. Define the Input Schema
class FAISSSearchInput(BaseModel):
    """Input schema for the FAISS Search Tool."""
    query: str = Field(..., description="The natural language query to search in the database.")

# 2. Define the Custom Tool Class
class FAISSRetrievalTool(BaseTool):
    name: str = "local_knowledge_base_search"
    description: str = (
        "Search the local FAISS database for technical documentation. "
        "Returns the top 5 most relevant chunks including metadata."
    )
    args_schema: Type[BaseModel] = FAISSSearchInput

    # Instance variables to hold the loaded index
    vector_store: any = None

    def __init__(self, folder_path: str, index_name: str = "index", **kwargs):
        super().__init__(**kwargs)
        # Load the index once during initialization
        embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en")
        self.vector_store = FAISS.load_local(
            'vector_database',
            embeddings,
            # index_name=index_name,
            allow_dangerous_deserialization=True
        )

    def _run(self, query: str) -> str:
        """Synchronous search logic."""
        # Retrieve top 5 similar chunks
        retriever = self.vector_store.as_retriever(search_kwargs={'k':5})
        docs = retriever.invoke(query)
        # docs = self.vector_store.similarity_search(query, k=5)

        # Format the output for the Agent
        results = []
        for i, doc in enumerate(docs, 1):
            source = doc.metadata.get('source', 'Unknown')
            page = doc.metadata.get('page', 'N/A')
            content = doc.page_content.replace("\n", " ")
            results.append(f"Result {i} (Source: {source}, Page: {page}):\n{content}\n")

        return "\n---\n".join(results)

    async def _arun(self, query: str) -> str:
        """Async implementation (optional, but good for CrewAI performance)."""
        # FAISS search is CPU-bound, so you can run it in a thread or just call _run
        return self._run(query)