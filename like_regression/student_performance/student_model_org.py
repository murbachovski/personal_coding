import os
import random
import tensorflow as tf
import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers, callbacks
import warnings
warnings.filterwarnings('ignore')  # 경고 메시지 무시

# ✅ 시드 고정
def set_seed(seed=42):
    os.environ['PYTHONHASHSEED'] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)

set_seed(32)

# 학생 성적 데이터 로드 (StudentID를 인덱스로 설정)
students_data = pd.read_csv('student_performance/student_performance_data.csv', index_col='StudentID')

# 결측치 제거 (실제 적용은 안 됨 — inplace 옵션 없기 때문)
students_data.dropna()

# 데이터프레임 정보 출력
students_data.info()

# 0~1 범위로 정규화하고, 모델 학습에 필요 없는 열 제거
def normalize_and_clean(dataset:pd.DataFrame):
    dataset = dataset.drop(columns=['Age', 'Gender', 'GradeClass', 'Ethnicity'])  # 관련 없는 열 제거
    for col in dataset.columns:
        if dataset[col].nunique() > 1:  # 고유값이 하나뿐인 열은 정규화 생략
            max_ = dataset[col].max()
            min_ = dataset[col].min()
            dataset[col] = (dataset[col] - min_) / (max_ - min_)
        else:
            dataset[col] = 0  # 고유값이 하나인 경우 0으로 설정
    normalized_dataset = dataset
    return normalized_dataset

# 테스트셋 분리 (앞의 15명)
df_test = students_data.iloc[:15]

# 훈련/검증용 데이터셋에서 테스트셋 제거
students_data = students_data.drop(students_data.index[:15])

# 훈련셋 80%, 검증셋 20%로 분리
df_train = students_data.sample(frac=0.8)
df_valid = students_data.drop(df_train.index)

# 훈련셋, 검증셋 정규화 및 불필요한 열 제거
df_train = normalize_and_clean(df_train)
df_valid = normalize_and_clean(df_valid)

# 특성과 정답 분리
X_train = df_train.drop('GPA', axis=1)
X_valid = df_valid.drop('GPA', axis=1)
y_train = df_train['GPA']
y_valid = df_valid['GPA']

# 정규화된 훈련셋 출력
# print(X_train)
# print(X_train.shape)

# 조기 종료 콜백 설정 (성능 향상 없을 시 조기 종료)
early_stopping = callbacks.EarlyStopping(
    min_delta = 0.001,
    patience = 20,
    restore_best_weights = True
)

# 모델 구성
model = keras.Sequential([
    layers.Input(shape=[9]),  # 입력 노드 수 = 9개 특성
    layers.BatchNormalization(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(32, activation='relu'),
    layers.BatchNormalization(),
    layers.Dense(256, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.BatchNormalization(),
    layers.Dense(1),  # 출력: 예측된 GPA
])

# 옵티마이저 및 손실함수 설정
opt = keras.optimizers.Adam(learning_rate=0.02)
model.compile(
    optimizer=opt,
    loss='mae'  # 평균 절대 오차
)

# 모델 학습
history = model.fit(
    X_train, y_train,
    validation_data=(X_valid, y_valid),
    batch_size=32,
    epochs=500,
    callbacks = [early_stopping]
)

# 학습 과정 시각화 (손실 값)
history_df = pd.DataFrame(history.history)
history_df.loc[1:, ['loss', 'val_loss']].plot()
plt.show()

# 정규화된 예측 결과를 실제 GPA 범위(0~4)로 변환
def unnormalize_results(predictions:np.array):
    predicted_gpa = []
    for gpa in predictions:
        predicted_gpa.append(np.absolute(gpa[0] * 4))  # GPA는 0~1 정규화 상태 → 4를 곱해 원래 값으로 복원
    return predicted_gpa

# 예측 성능 평가
total_deviation = 0

print("실제 GPA:               예측 GPA:")
for prediction, actual in zip(unnormalize_results(model.predict(np.array(normalize_and_clean(df_test.drop(columns=['GPA']))))), np.array(df_test['GPA'])):
    print(f'{actual}      -       {prediction}')
    total_deviation += np.absolute(actual-prediction)

print(f'총 오차 합계: {total_deviation}')
print(f'평균 오차: {total_deviation/15}')

## 모델 개요
# 이 모델은 완벽하진 않지만, GPA 예측 범위 내에서 어느 정도 의미 있는 예측을 수행함.

## 결론
# 본 문서는 학생 성과에 영향을 미치는 요인들을 통계적으로 분석하며,
# 학생의 환경과 습관이 향후 학업 성취도에 어떤 영향을 주는지 신경망 모델을 통해 예측을 시도함.

# 기존 성능
# Total deviation: 4.39344392454638
# Average deviation: 0.29289626163642535

# 모델 튜닝
# 총 오차 합계: 4.081451512044329
# 평균 오차: 0.2720967674696219
