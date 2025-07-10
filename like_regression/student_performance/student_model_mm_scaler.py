# ✅ MinMaxScaler 적용

import os
import random
import tensorflow as tf
import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler, RobustScaler
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

# ✅ 데이터 로드
students_data = pd.read_csv('student_performance/student_performance_data.csv', index_col='StudentID')
students_data = students_data.dropna()

# ✅ 테스트셋 분리 (앞의 15명)
df_test = students_data.iloc[:15].copy()
students_data = students_data.drop(df_test.index)

# ✅ 필요 없는 열 제거
drop_cols = ['Age', 'Gender', 'GradeClass', 'Ethnicity']
df_train = students_data.sample(frac=0.8, random_state=32)
df_valid = students_data.drop(df_train.index)

# ✅ 특성, 정답 분리
X_train = df_train.drop(columns=drop_cols + ['GPA'])
X_valid = df_valid.drop(columns=drop_cols + ['GPA'])
X_test  = df_test.drop(columns=drop_cols + ['GPA'])

y_train = df_train['GPA']
y_valid = df_valid['GPA']
y_test  = df_test['GPA']

# ✅ StandardScaler 적용
# scaler = StandardScaler()
scaler = MinMaxScaler()
# scaler = MaxAbsScaler()
# scaler = RobustScaler()

X_train = scaler.fit_transform(X_train)
X_valid = scaler.transform(X_valid)
X_test  = scaler.transform(X_test)

# ✅ 모델 구성
model = keras.Sequential([
    layers.Input(shape=[X_train.shape[1]]),  # 입력 특성 수 자동 적용
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
    layers.Dense(1)  # 출력: GPA 예측
])

# ✅ 컴파일
opt = keras.optimizers.Adam(learning_rate=0.02)
model.compile(
    optimizer=opt,
    loss='mae'
)

# ✅ 조기 종료 콜백
early_stopping = callbacks.EarlyStopping(
    min_delta=0.001,
    patience=50,
    restore_best_weights=True
)

# ✅ 모델 학습
history = model.fit(
    X_train, y_train,
    validation_data=(X_valid, y_valid),
    batch_size=32,
    epochs=500,
    callbacks=[early_stopping]
)

# ✅ 학습 시각화
history_df = pd.DataFrame(history.history)
history_df.loc[1:, ['loss', 'val_loss']].plot()
plt.title("Loss Curve")
plt.ylabel("MAE")
plt.xlabel("Epoch")
plt.grid()
plt.show()

# ✅ 예측 및 평가
preds = model.predict(X_test).flatten()

total_deviation = 0
print("실제 GPA:               예측 GPA:")
for actual, pred in zip(y_test, preds):
    print(f'{actual:.2f}      -       {pred:.2f}')
    total_deviation += abs(actual - pred)

print(f'\n총 오차 합계: {total_deviation}')
print(f'평균 오차: {total_deviation / len(y_test)}')

# MINMAX
# 총 오차 합계: 1.9896162748336792
# 평균 오차: 0.13264109194278717
