# 가상환경 생성
    # conda create -n likeimgtext python=3.11
    # pip install fastapi uvicorn python-multipart transformers torch pillow

from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch
import os

app = FastAPI()

# 템플릿 디렉토리 설정
templates = Jinja2Templates(directory="templates")

# 업로드 파일 저장 경로
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# 모델 및 프로세서 불러오기 (초기 1회만)
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# HTML 입력 폼 (GET)
@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("form.html", {"request": request, "caption": None})

# 이미지 업로드 및 캡션 처리 (POST)
@app.post("/caption", response_class=HTMLResponse)
async def generate_caption(request: Request, file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as f:
        f.write(await file.read())

    # 이미지 로딩 및 처리
    image = Image.open(file_location).convert("RGB")
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)

    return templates.TemplateResponse("form.html", {
        "request": request,
        "caption": caption,
        "image_path": f"/{file_location}"
    })

# 이미지 정적 파일 경로 제공
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")