## 🚀 프로젝트 설명

웹에서 영어 문장을 입력받아 `language_tool_python` 라이브러리를 활용해 문법과 맞춤법을 자동으로 교정해주는 FastAPI 기반 웹 서비스입니다.  
입력한 문장이 이미 깔끔하면 사용자에게 친절한 안내 메시지를 제공합니다.

---

## ⚙️ 환경 및 기술 스택

- **Backend**: FastAPI  
- **문법 교정 엔진**: language_tool_python (LanguageTool API 래퍼)  
- **Python 패키지**: fastapi, uvicorn, jinja2, python-multipart, language-tool-python  
- **Frontend**: Jinja2 템플릿 엔진 기반 HTML/CSS  
- **운영체제**: macOS (Java OpenJDK 설치 필요)  

---

## 🐍 가상환경 생성
```
conda create -n sen_corr python=3.9
```

## 🌈 패키지 설치
```
./setup.sh
```

## 💡 FastAPI 서버 실행
```
./run.sh
```

# 🖼️ Result Images
<p align="center">
  <img src="https://github.com/user-attachments/assets/c1086e00-4ee6-4a13-95ce-dbebdbde22a4" width="1000">
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/a404619a-c45e-4e7f-a21d-fbe17da7b240" width="1000">
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/901a76e6-32fd-4d11-bb34-aa56a07ffc60" width="1000">
</p>


---
