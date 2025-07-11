# 🚀 음성 파일 요약 및 번역 프로젝트

---

## 🚀 프로젝트 설명

음성 파일을 업로드하면 Whisper 모델로 음성을 텍스트로 변환하고, 변환된 텍스트를 Transformers 기반 요약 모델로 요약한 뒤, 최종적으로 Google Translate를 통해 한국어로 번역하는 웹 서비스 프로젝트입니다.  
FastAPI와 Jinja2를 이용해 간단한 웹 인터페이스를 제공하며, 사용자가 음성 파일을 쉽게 업로드하고 결과를 확인할 수 있도록 구현했습니다.

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

## 🐍 가상환경 생성

```bash
conda create -n stt python=3.9
conda activate stt
pip install fastapi uvicorn whisper transformers googletrans==4.0.0-rc1 jinja2


## 💡 FastAPI 서버 실행
```
./run.sh
```

# 🖼️ Result Images
<p align="center">
  <img src="https://github.com/user-attachments/assets/c1086e00-4ee6-4a13-95ce-dbebdbde22a4" width="700">
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/a404619a-c45e-4e7f-a21d-fbe17da7b240" width="700">
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/901a76e6-32fd-4d11-bb34-aa56a07ffc60" width="700">
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/d7112040-a81f-4e0c-9c21-b68555b54562" width="700">
</p>

---
