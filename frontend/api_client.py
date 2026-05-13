import requests
from fastapi import Body

BASE_URL = "http://localhost:8000"

def send_query(query: str ):
    try:
        response = requests.post(
            f"{BASE_URL}/query",
            params={"query": query}
        )
        return response.json()
    except Exception as e:
        return {"error": str(e)}


def upload_file(file):
    try:
        files = {"file": (file.name, file, file.type)}
        response = requests.post(
            f"{BASE_URL}/upload",
            files=files
        )
        return response.json()
    except Exception as e:
        return {"error": str(e)}