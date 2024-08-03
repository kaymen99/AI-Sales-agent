import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-base-en-v1.5")

vectorstore = Chroma(persist_directory="db", embedding_function=embeddings)

# Semantic vector search
vectorstore_retreiver = vectorstore.as_retriever(search_kwargs={"k": 3})

template = """
Your are an assistant at TechNerds.
TechNerds's business is about: Selling high-quality computer equipment, including laptops, desktops, monitors, keyboards, etc.
Your goal is to provide accurate information about our products and services. 
Use the following pieces of retrieved context to answer the question. 
Do not mention having access to context in your output.
If you don't know the answer, just say that I don't know.
Question: {question}
Context: {context}
"""
prompt = ChatPromptTemplate.from_template(template)

llm = ChatGroq(model="mixtral-8x7b-32768", api_key=os.getenv("GROQ_API_KEY"))

# build retrieval chain using LCEL
# this will take the user query and generate the answer
rag_chain = (
    {"context": vectorstore_retreiver, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

query = "Do you have shipment to Paris?"
result = rag_chain.invoke(query)
print(result)
