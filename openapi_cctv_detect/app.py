# OpenAPI
    # ITS
        # https://its.go.kr/opendata/
# 가상환경 생성
    # conda create -n oapi python=3.9
    # pip install pandas opencv-python ultralytics

# 📦 필요한 라이브러리 불러오기
import json
import pandas as pd
import cv2
import urllib.request
from ultralytics import YOLO

# 🔑 1. Open API 인증키
api_key = ""

# 🛣️ 2. 도로 유형 선택 (its: 일반도로 / ex: 고속도로)
road_type = "its"

# 🌍 3. CCTV 요청 범위 설정 (경도/위도 범위)
minX, maxX = 120.95, 127.02
minY, maxY = 30.55, 37.69

# 📂 4. 응답 포맷 설정
response_type = "json"

# 🌐 5. CCTV 정보 요청 URL 구성
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

# 🔍 8. 테스트용 CCTV 스트리밍 URL 하나 선택
test_url = cctv_df['cctvurl'][256]

# 📹 9. 영상 스트림 열기
cap = cv2.VideoCapture(test_url)

# 🤖 10. YOLO 모델 로드 (로컬에 있는 모델 경로 사용)
model = YOLO("yolo11n.pt")

# 🧠 11. 영상 프레임마다 객체 탐지 수행
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("비디오 프레임 읽기 실패 또는 종료")
        break
    
    # YOLO 객체 탐지
    results = model(frame)
    annotated_frame = results[0].plot()

    # 영상 창 조정 및 출력
    cv2.namedWindow("OPENAPI_CCTV_YOLO", cv2.WINDOW_NORMAL)
    cv2.imshow("OPENAPI_CCTV_YOLO", annotated_frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("사용자 종료 요청 (q 키)")
        break

# 🎬 자원 정리
cap.release()
cv2.destroyAllWindows()