# 프로젝트 설명
```
ITS OpenAPI 기반 실시간 CCTV 영상에서 YOLO를 이용한 객체 탐지 및 카운팅
```

# OpenAPI
```
ITS
https://its.go.kr/opendata/
```

# 가상환경 생성
```
conda create -n oapi python=3.9
pip install pandas opencv-python ultralytics
pip install pandas opencv-python ultralytics shapely lap
```

# 실행
```
⚠️ 주의: ultralytics/solutions 내부에서 similarity_search 관련 import 오류가 발생할 경우,
ultralytics/solutions/__init__.py 에서 아래 라인을 주석 처리:
from .similarity_search import SearchApp, VisualAISearch
```

# OpenAPI 설명
<p align="center">
  <img src="https://github.com/user-attachments/assets/9e80f6a1-f7c2-47ee-b162-a59e9cc888fb" width="1000">
</p>

# 결과
<p align="center">
  <img src="https://github.com/user-attachments/assets/801b09fe-5044-459b-8e5f-274bcd517540" width="500">
  <img src="https://github.com/user-attachments/assets/6b97ad40-ff41-46dd-b662-d1bb4b31c40a" width="500">
</p>
