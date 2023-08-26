from fastapi import FastAPI, Request
from urllib.parse import unquote
import scraper

app = FastAPI()

@app.get("/")
async def root(request:Request):
    return {"message": "Scraper for www.gob.bo", 
            "documentation": str(request.url)+"docs"}

@app.get("/subtitles/{url:path}")
async def details(url:str):
    url = unquote(url)
    subs = scraper.h2(url)
    return { "subtitles": subs}

@app.get("/details/{url:path}")
async def details(url:str):
    url = unquote(url)
    res = scraper.between_h2(url)
    return { "details": res}

