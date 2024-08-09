import os
from pydantic import Field
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from src.prompts.prompts import RAG_SEARCH_PROMPT_TEMPLATE
from .base_tool import BaseTool


def load_retriever():
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-base-en-v1.5")
    vectorstore = Chroma(persist_directory="db", embedding_function=embeddings)
    vectorstore_retreiver = vectorstore.as_retriever(search_kwargs={"k": 3})
    prompt = ChatPromptTemplate.from_template(RAG_SEARCH_PROMPT_TEMPLATE)

    llm = ChatGroq(model="mixtral-8x7b-32768", api_key=os.getenv("GROQ_API_KEY"))
    app = (
        {"context": vectorstore_retreiver, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return app


def get_store_info(query: str) -> str:
    app = load_retriever()
    response = app.invoke(query)
    return str(response)


class GetStoreInfo(BaseTool):
    """
    A tool that retrieves information about TechNerds' business, services, and products based on the provided query.
    """

    query: str = Field(description="Query string")

    def run(self):
        return get_store_info(self.query)
