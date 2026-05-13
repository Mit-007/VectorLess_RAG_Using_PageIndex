from fastapi import File , UploadFile ,BackgroundTasks
from fastapi import APIRouter,Depends
from fastapi import HTTPException
from app.services.upload_file import document_submit
from app.services.tree_generate_status import generate_tree_status
from app.utils.excel_to_pdf import excel_to_pdf
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True 
)

router = APIRouter(prefix="", tags=["RAG_model_Q&A"])

@router.post("/upload")
async def upload_file(background_tasks: BackgroundTasks,file: UploadFile = File(...)):
    try:
        if not file.filename:
            raise HTTPException(status_code=400, detail="No file name provided")
        
        logging.info("=============================  start process  ===========================================")
       
        foldar_path = "data/uploads"

        os.makedirs(foldar_path,exist_ok=True)

        file_path = os.path.join(foldar_path,file.filename)

        content = await file.read()
    
        if file.filename.endswith(".json"):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content.decode("utf-8"))
        else:
            with open(file_path, "wb") as f:
                f.write(content)

        doc_id = document_submit(file_path)

        logging.info("Upload completed")

        # tree_result = await generate_tree_status(doc_id)

        # logging.info(tree_result)

        logging.info("=============================  end process  ===========================================")

        return {
            "filename": file.filename,
            "doc_id" : doc_id,
            "message":"file uploaded sucessfully !!"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))