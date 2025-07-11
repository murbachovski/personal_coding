from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import whisper
from transformers import pipeline
from googletrans import Translator
import os
import uuid

# 모델 로드
whisper_model = whisper.load_model("base")
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", framework="pt")
translator = Translator()

# FastAPI 앱 및 템플릿 설정
app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload", response_class=HTMLResponse)
async def upload(request: Request, file: UploadFile = File(...)):
    # 1. 임시 저장
    filename = f"temp_{uuid.uuid4().hex}.mp3"
    with open(filename, "wb") as f:
        f.write(await file.read())

    # 2. Whisper로 텍스트 추출
    transcript = whisper_model.transcribe(filename)["text"]

    # 3. 요약
    if len(transcript) < 30:
        summary = transcript
    else:
        summary = summarizer(transcript, max_length=130, min_length=30, do_sample=False)[0]["summary_text"]

    # 4. 번역
    translated = translator.translate(summary, src='en', dest='ko').text

    # 5. 파일 제거
    os.remove(filename)

    # 6. 결과 반환
    return templates.TemplateResponse("index.html", {
        "request": request,
        "transcript": transcript,
        "summary": summary,
        "translated": translated
    })
