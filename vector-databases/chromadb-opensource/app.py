from dotenv import load_dotenv
import os

load_dotenv()

CHROMADB_API_KEY = os.getenv("CHROMA_API_KEY")