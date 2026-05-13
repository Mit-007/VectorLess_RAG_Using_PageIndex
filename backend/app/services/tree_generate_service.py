import logging
from pageindex import PageIndexClient
import pageindex.utils as utils
from dotenv import load_dotenv
from app.core.config import PAGEINDEX_API_KEY

def generate_tree(doc_id):

    pi_client = PageIndexClient(api_key=PAGEINDEX_API_KEY)

    tree_result = pi_client.get_tree(doc_id=doc_id,node_summary=True)

    if tree_result.get("status")=="completed":
        return tree_result

    # utils.print_tree(tree_result)

    logging.INFO("tree not ready now")

    return tree_result
