from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from src.config import VECTOR_DIR

EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

def get_embeddings():
    return HuggingFaceEmbeddings(model_name=EMBED_MODEL)

def build_vector_store(texts):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    docs = []
    for text in texts:
        chunks = splitter.split_text(text)
        docs.extend(chunks)
    embeddings = get_embeddings()
    vectordb = FAISS.from_texts(docs, embedding=embeddings)
    vectordb.save_local(str(VECTOR_DIR))
    return vectordb

def load_vector_store():
    embeddings = get_embeddings()
    return FAISS.load_local(
        str(VECTOR_DIR),
        embeddings,
        allow_dangerous_deserialization=True
    )

def retrieve_context(vectordb, zodiac_sign: str, k: int = 4):
    query = f"{zodiac_sign} zodiac personality traits love career strengths weaknesses daily guidance"
    docs = vectordb.similarity_search(query, k=k)
    context = "\n\n".join([d.page_content for d in docs])
    return context, docs