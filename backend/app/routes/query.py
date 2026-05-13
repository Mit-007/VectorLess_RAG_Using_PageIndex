from datetime import datetime
from fastapi import APIRouter
from app.services.rag_servisec import query_answer
import os
import logging
import asyncio

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True 
)

router = APIRouter(prefix="", tags=["RAG_model_Q&A"])

@router.post("/query")
async def ask_query(query : str):

    
    logging.info("=============================  start process  ===========================================")
    result = await query_answer(query)
    logging.info("=============================  end process  =============================================")


    return {
        "question": query,
        "message":result
    }