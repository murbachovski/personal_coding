## 🚀 프로젝트 설명

음성 파일을 Whisper로 텍스트 변환 후 요약하고, Google Translate로 번역해 FastAPI 웹에서 결과를 제공하는 서비스

---

## ⚙️ 환경 및 기술 스택

- Python 3.9+
- FastAPI (웹 서버)
- Whisper (음성 → 텍스트)
- Huggingface Transformers (텍스트 요약)
- googletrans (영어 → 한국어 번역)
- Jinja2 (템플릿 렌더링)
- Uvicorn (ASGI 서버)

---

## 🐍 가상환경 생성 및 설치
```
conda create -n stt python=3.9
conda activate stt
pip install fastapi uvicorn whisper transformers googletrans==4.0.0-rc1 jinja2
```

## 💡 FastAPI 서버 실행
```
./run.sh
```

# 🖼️ Result Images
<p align="center">
  <img src="https://github.com/user-attachments/assets/092b1609-2549-4ff0-96c4-a0e7ada0ca7f" width="700">
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/90128ca0-acc2-47ec-b8cd-9b242e6afb41" width="700">
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/cb157988-0f5d-47ee-8a79-e679865e5bb1" width="700">
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/244f0f1b-b527-46a1-9808-dfc1f4bcc94e" width="700">
</p>

---
