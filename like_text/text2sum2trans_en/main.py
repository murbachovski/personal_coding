# 가상환경 생성
    # conda create -n liketext python=3.10
    # pip install fastapi uvicorn transformers torch googletrans==4.0.0-rc1
    # pip install python-multipart
# 웹 실행
    # uvicorn main:app --reload

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from transformers import pipeline
from googletrans import Translator
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# HTML 템플릿 위치 지정
templates = Jinja2Templates(directory="templates")

# 요약 모델 로드
summarizer = pipeline("summarization", model="t5-small")

# 번역 함수
def translate_text(text):
    translator = Translator()
    translation = translator.translate(text, dest='ko')
    return translation.text

# HTML 입력 폼
@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

# 요약 및 번역 처리
@app.post("/summarize", response_class=HTMLResponse)
async def summarize_text(request: Request, input_text: str = Form(...)):
    summary_result = summarizer(
    input_text,
    min_length=5,
    max_length=30,
    do_sample=False  # 랜덤성 제거
)
    summary = summary_result[0]['summary_text']
    translated = translate_text(summary)

    return templates.TemplateResponse("form.html", {
        "request": request,
        "original": input_text,
        "summary": summary,
        "translated": translated
    })

## 예문 ##
'''
A special 25th anniversary edition of the extraordinary international bestseller, including a new Foreword by Paulo Coelho.

Combining magic, mysticism, wisdom and wonder into an inspiring tale of self-discovery, The Alchemist has become a modern classic, selling millions of copies around the world and transforming the lives of countless readers across generations.

Paulo Coelho's masterpiece tells the mystical story of Santiago, an Andalusian shepherd boy who yearns to travel in search of a worldly treasure. His quest will lead him to riches far different-and far more satisfying-than he ever imagined. Santiago's journey teaches us about the essential wisdom of listening to our hearts, of recognizing opportunity and learning to read the omens strewn along life's path, and, most importantly, to follow our dreams.
'''