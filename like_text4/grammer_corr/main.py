from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import language_tool_python

app = FastAPI()
templates = Jinja2Templates(directory="templates")

tool = language_tool_python.LanguageTool('en-US')

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "original": "", "corrected": "", "message": ""})

@app.post("/correct", response_class=HTMLResponse)
async def correct(request: Request, text: str = Form(...)):
    corrected = tool.correct(text)

    message = ""
    if text.strip() == corrected.strip():
        message = "🎉 문장이 깔끔해요! 오류가 발견되지 않았습니다."

    return templates.TemplateResponse("index.html", {
        "request": request,
        "original": text,
        "corrected": corrected if text.strip() != corrected.strip() else "",
        "message": message
    })
