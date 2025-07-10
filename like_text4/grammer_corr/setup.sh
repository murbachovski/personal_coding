#!/bin/bash

echo "🚀 FastAPI 기반 영문법 교정기 설치 시작"

# 0. Python 패키지 설치
echo "📦 Python 패키지 설치 중..."
pip install fastapi uvicorn jinja2 language-tool-python python-multipart

# 1. OpenJDK 설치
echo "☕️ OpenJDK 설치 중 (macOS)..."
brew install openjdk

# 2. 심볼릭 링크 생성
echo "🔗 Java 경로 설정 중..."
sudo ln -sfn /opt/homebrew/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk

# 3. 환경 변수 설정
echo '🔧 환경 변수 설정 중...'
echo 'export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"' >> ~/.zprofile

# 4. 환경 반영
source ~/.zprofile

# 5. Java 설치 확인
echo "✅ Java 버전 확인:"
java -version

echo "🎉 설치 완료! uvicorn main:app --reload 로 서버 실행하세요."
