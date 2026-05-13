from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PAGEINDEX_API_KEY=os.getenv("PAGEINDEX_API_KEY")
DOC_ID=os.getenv("DOC_ID")