import os
from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

print("Loading Docs...")
loader = DirectoryLoader("./files")
docs = loader.load()

print("Splitting Docs...")
doc_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=200)
doc_chunks = doc_splitter.split_documents(docs)

print("Loading embedding model...")
embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-base-en-v1.5")

print("Creating vector store...")
vectorstore = Chroma.from_documents(doc_chunks, embeddings, persist_directory="db")

# Semantic vector search
vectorstore_retreiver = vectorstore.as_retriever(search_kwargs={"k": 3})

# Keyword search
keyword_retriever = BM25Retriever.from_documents(doc_chunks)
keyword_retriever.k = 3

# Hybride search
ensemble_retriever = EnsembleRetriever(
    retrievers=[vectorstore_retreiver, keyword_retriever], weights=[0.3, 0.7]
)

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

llm = ChatGroq(model="llama3-70b-8192", api_key=os.getenv("GROQ_API_KEY"))

# build retrieval chain using LCEL
# this will take the user query and generate the answer
rag_chain = (
    {"context": ensemble_retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

query = "What are the prices of laptops?"
result = rag_chain.invoke(query)
print(result)
