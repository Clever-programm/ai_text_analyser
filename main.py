from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import Optional


class TextFile(BaseModel):
    filename: Optional[str] = None
    words_count: Optional[int] = None


app = FastAPI()


@app.get("/")
async def status():
    """
    Simple function to get status
    :return: server status
    """

    return {"status": "ok"}

@app.post("/send_txt")
async def handle_txt(file: UploadFile):
    """
    Handle uploaded txt file. Analyse text
    :param file: uploaded file
    :return: information about file and text
    """

    if file.content_type != "text/plain":
        raise HTTPException(status_code=400, detail="Only .txt files are allowed")
    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="File must have .txt extension")

    content = await file.read()
    text = content.decode("utf-8")

    res = TextFile()
    res.filename = file.filename
    res.words_count = len(text.split())

    return res
