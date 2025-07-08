# 📌 ITS OpenAPI + YOLO 객체 카운팅 프로젝트
# 출처: https://its.go.kr/opendata/

# ▶ 가상환경 생성 및 필수 패키지 설치
# conda create -n oapi python=3.9
# pip install pandas opencv-python ultralytics shapely lap

# ⚠️ 주의: ultralytics/solutions 내부에서 similarity_search 관련 import 오류가 발생할 경우,
#          ultralytics/solutions/__init__.py 에서 아래 라인을 주석 처리:
#          from .similarity_search import SearchApp, VisualAISearch

# 📦 라이브러리 불러오기
import json
import pandas as pd
import cv2
import urllib.request
from ultralytics import solutions  # ObjectCounter 사용

# 🔐 1. ITS OpenAPI 인증키 입력
api_key = "db5c00dc1fce45c49049bff225a0fea6"

# 🛣️ 2. 도로 유형 선택 (its: 일반 도로 / ex: 고속도로)
road_type = "its"

# 🌍 3. CCTV 요청 범위 설정 (위도/경도)
minX, maxX = 120.95, 127.02
minY, maxY = 30.55, 37.69

# 📂 4. 응답 데이터 포맷 (json 권장)
response_type = "json"

# 🌐 5. CCTV 정보 요청 URL 생성
url = (
    f"https://openapi.its.go.kr:9443/cctvInfo?"
    f"apiKey={api_key}&type={road_type}&cctvType=1"
    f"&minX={minX}&maxX={maxX}&minY={minY}&maxY={maxY}"
    f"&getType={response_type}"
)

# 📡 6. API 요청 및 응답 수신
response = urllib.request.urlopen(url)
json_str = response.read().decode("utf-8")
json_data = json.loads(json_str)

# 📊 7. JSON 응답을 DataFrame으로 변환
cctv_df = pd.json_normalize(json_data["response"]["data"], sep='')

# 🔍 8. 테스트용 CCTV 스트리밍 URL 선택
test_url = cctv_df['cctvurl'][128]

# 📹 9. 영상 스트림 열기
cap = cv2.VideoCapture(test_url)

# 🔲 10. 객체 카운팅 영역 좌표 설정 (좌상단, 우하단) - 640x480 기준
count_points = [(201, 225), (495, 270)]

# 🤖 11. YOLO 기반 객체 카운터 초기화
counter = solutions.ObjectCounter(
    model="yolo11n.pt",   # YOLO 모델 경로 (로컬)
    show=True,            # 실시간 시각화 창 띄우기
    region=count_points   # 지정 영역 안의 객체만 카운트
)

# 🧠 12. 영상 프레임 처리 루프
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("비디오 프레임 읽기 실패 또는 종료")
        break

    # 프레임 크기 YOLO 입력 크기에 맞게 리사이즈
    re_frame = cv2.resize(frame, (640, 480))

    # YOLO로 객체 탐지 및 카운트 수행
    results = counter(frame)

    # 'q' 키 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("사용자 종료 요청 (q 키)")
        break

# 🎬 13. 영상 스트림 및 OpenCV 창 종료
cap.release()
cv2.destroyAllWindows()
