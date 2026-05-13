from pageindex import PageIndexClient
from dotenv import load_dotenv
from app.core.config import PAGEINDEX_API_KEY

def document_submit(path):

    pi_client = PageIndexClient(api_key=PAGEINDEX_API_KEY)

    result = pi_client.submit_document(path)

    return result["doc_id"]
