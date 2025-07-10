# 🖼️ OCR 웹 서비스 (FastAPI + Tesseract)

이미지를 업로드하면 Tesseract OCR을 이용해 텍스트(영어/한글)를 추출해주는  
**FastAPI 기반의 간단하고 직관적인 웹 애플리케이션**입니다.

---

## 🚀 프로젝트 설명

- 사용자는 웹에서 이미지를 업로드하면
- 서버는 Tesseract OCR을 통해 텍스트를 추출하고
- 웹 페이지에서 이미지와 추출된 텍스트를 함께 확인할 수 있습니다.

---

## ⚙️ 환경 및 기술 스택

- **Backend**: FastAPI
- **OCR 엔진**: Tesseract (brew 설치)
- **Frontend**: Jinja2 (템플릿 엔진), HTML5, CSS3
- **Python OCR Wrapper**: pytesseract
- **Image 처리**: Pillow

---

## 🐍 가상환경 생성 및 실행 방법

```
# 1. 가상환경 생성 및 활성화
conda create -n ocr python=3.9

# 2. 필요한 패키지 설치(Mac M1)
# brew install tesseract
# brew install tesseract-lang
# pip install pytesseract pillow

# 3. FastAPI 서버 실행
uvicorn main:app --reload
./run.sh
```

# 🖼️ Result Images
<p align="center">
  <img src="https://github.com/user-attachments/assets/33669e67-3bc5-4eb0-ad60-5b61974dad54" width="190">
  <img src="https://github.com/user-attachments/assets/d5eebf20-83a5-420e-a9b5-1f5a39164fb9" width="190">
</p>

---
