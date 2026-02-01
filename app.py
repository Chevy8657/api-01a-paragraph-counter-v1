from fastapi import FastAPI, Query
from pydantic import BaseModel
import re

app = FastAPI(title="Paragraph Counter", version="v1")

class Health(BaseModel):
    ok: bool

class ParagraphCountResponse(BaseModel):
    input: str
    paragraph_count: int

@app.get("/health", response_model=Health)
def health():
    return {"ok": True}

@app.get("/v1/paragraph-count", response_model=ParagraphCountResponse)
def paragraph_count(text: str = Query(..., description="Text to count paragraphs for")):
    # Paragraphs separated by one or more blank lines
    paragraphs = [p for p in re.split(r"\n\s*\n", text.strip()) if p]
    return {"input": text, "paragraph_count": len(paragraphs)}
