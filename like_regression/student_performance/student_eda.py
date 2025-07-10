import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# 데이터 불러오기
students_data = pd.read_csv('student_performance/student_performance_data.csv', index_col='StudentID')
students_data.dropna()

# 1. 나이 분포
plt.figure()
sns.histplot(data=students_data, x='Age', discrete=True)
plt.xticks(students_data['Age'].unique())
plt.title("Age Distribution")
plt.savefig("01_eda_age_distribution.png")

# 2. GPA 분포
plt.figure()
sns.kdeplot(data=students_data, x='GPA', fill=True)
plt.title("GPA Density Plot")
plt.savefig("02_eda_gpa_distribution.png")

# 3. 비교과 활동 파이 차트
plt.figure()
extracurricular_groups = students_data.groupby('Extracurricular').count()
plt.pie(
    data=extracurricular_groups,
    x='Age',
    labels=['No extracurricular', 'Any extracurricular'],
    autopct='%.0f%%',
    explode=[.01, .01]
)
plt.title("Extracurricular Participation")
plt.savefig("03_eda_extracurricular_pie.png")

# 4. 학습 시간 vs GPA (튜터링별)
sns.lmplot(data=students_data, x='StudyTimeWeekly', y='GPA', hue='Tutoring')
plt.title("Study Time vs GPA (Tutoring)")
plt.savefig("04_eda_studytime_vs_gpa.png")

# 5. 결석 vs GPA (튜터링별)
sns.lmplot(data=students_data, x='Absences', y='GPA', hue='Tutoring')
plt.title("Absences vs GPA (Tutoring)")
plt.savefig("05_eda_absences_vs_gpa.png")

# 6. 튜터링 여부에 따른 GPA
plt.figure()
sns.boxplot(data=students_data, x='Tutoring', y='GPA')
plt.title("GPA by Tutoring")
plt.savefig("06_eda_gpa_by_tutoring.png")

# 7. 비교과 활동 여부에 따른 GPA
plt.figure()
sns.boxplot(data=students_data, x='Extracurricular', y='GPA')
plt.title("GPA by Extracurricular")
plt.savefig("07_eda_gpa_by_extracurricular.png")

# 8. 성별에 따른 GPA
plt.figure()
sns.boxplot(data=students_data.replace({'Gender':{0:'Male', 1:'Female'}}), x='Gender', y='GPA')
plt.title("GPA by Gender")
plt.savefig("08_eda_gpa_by_gender.png")

# 9. 부모 학력 수준에 따른 GPA
plt.figure()
sns.boxplot(data=students_data, x='ParentalEducation', y='GPA')
plt.title("GPA by Parental Education")
plt.savefig("09_eda_gpa_by_parentaledu.png")

# 10. 부모 지원 여부에 따른 GPA
plt.figure()
sns.boxplot(data=students_data, x='ParentalSupport', y='GPA')
plt.title("GPA by Parental Support")
plt.savefig("10_eda_gpa_by_parentsupport.png")

# 11. 상관관계 히트맵
plt.figure(figsize=(10, 8))
sns.heatmap(data=students_data.corr(), annot=True, fmt=".2f", cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.savefig("11_eda_correlation_heatmap.png")
