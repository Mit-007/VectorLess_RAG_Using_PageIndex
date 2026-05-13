import logging
import asyncio
from pageindex import PageIndexClient
from dotenv import load_dotenv
from app.core.config import PAGEINDEX_API_KEY

async def generate_tree_status(doc_id):

    pi_client = PageIndexClient(
        api_key=PAGEINDEX_API_KEY
    )

    while True:

        tree_result = pi_client.get_tree(
            doc_id=doc_id,
            node_summary=True
        )

        status = tree_result.get("status")

        logging.info(f"Tree Status: {status}")

        if status == "completed":

            return "tree_generated"

        elif status == "processing":

            logging.info(
                "Tree not ready, waiting 5 sec..."
            )

            await asyncio.sleep(5)

        else:
            raise Exception(
                f"Unexpected status: {status}"
            )