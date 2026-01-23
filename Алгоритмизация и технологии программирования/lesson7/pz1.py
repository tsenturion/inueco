# Практическое задание: Подготовка и очистка медицинского датасета

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder # type: ignore
import matplotlib.pyplot as plt
import seaborn as sns # type: ignore

def load_and_explore_data(filepath):
    """Загрузка и первичный анализ данных"""
    return pd.read_csv(filepath)

def clean_data(reader):
    """Основная функция очистки данных"""

    print(reader.size)
    print(reader.dtypes)
    print(reader.describe())
    print(reader['stroke'].value_counts())

    # Обработка пропусков
    print(reader.isnull().sum())

    median_bmi = reader['bmi'].median()
    reader.fillna({'bmi': median_bmi}, inplace=True)

    print(reader.isnull().sum())

    # Обработка категориальных переменных
    reader['gender'] = reader['gender'].str.lower().str.strip()
    reader['ever_married'] = reader['ever_married'].str.lower().str.strip()
    reader['work_type'] = reader['work_type'].str.lower().str.strip()
    reader['Residence_type'] = reader['Residence_type'].str.lower().str.strip()
    reader['smoking_status'] = reader['smoking_status'].str.lower().str.strip()

    reader = reader[reader['gender'] != 'other']

    valid_smoking_status = ['never smoked', 'formerly smoked', 'smokes', 'unknown']
    reader = reader[reader['smoking_status'].isin(valid_smoking_status)]
    print(reader['smoking_status'].value_counts())

    # Обработка выбросов
    Q1 = reader[['age', 'avg_glucose_level', 'bmi']].quantile(0.25)
    Q3 = reader[['age', 'avg_glucose_level', 'bmi']].quantile(0.75)
    IQR = Q3 - Q1
    outliers = ((reader[['age', 'avg_glucose_level', 'bmi']] < (Q1 - 1.5 * IQR)) | (reader[['age', 'avg_glucose_level', 'bmi']] > (Q3 + 1.5 * IQR)))
    print(outliers.sum())

    lower_bound = reader[['avg_glucose_level', 'bmi']].quantile(0.01)
    upper_bound = reader[['avg_glucose_level', 'bmi']].quantile(0.99)
    reader[['avg_glucose_level', 'bmi']] = reader[['avg_glucose_level', 'bmi']].clip(lower=lower_bound, upper=upper_bound, axis=1)

    reader = reader[reader['age'] <= 120]
    print(reader.describe())

    # Нормализация и кодирование
    scaler = StandardScaler()
    reader[['age', 'avg_glucose_level', 'bmi']] = scaler.fit_transform(reader[['age', 'avg_glucose_level', 'bmi']])
    print(reader[['age', 'avg_glucose_level', 'bmi']].describe())

    le_gender = LabelEncoder()
    reader['gender'] = le_gender.fit_transform(reader['gender'])
    le_married = LabelEncoder()
    reader['ever_married'] = le_married.fit_transform(reader['ever_married'])
    le_residence = LabelEncoder()
    reader['Residence_type'] = le_residence.fit_transform(reader['Residence_type'])
    reader = pd.get_dummies(reader, columns=['work_type', 'smoking_status'], drop_first=True)

    # Удаление ненужных столбцов
    reader.drop(columns=['id'], inplace=True)

    print(reader.isnull().sum())
    print(reader['stroke'].value_counts())

    return reader

# Основной блок выполнения
if __name__ == "__main__":
    reader = load_and_explore_data('healthcare-dataset-stroke-data.csv')

    cleaned_data = clean_data(reader)

    plt.figure(figsize=(32,32))
    correlation_matrix = cleaned_data.corr()
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.savefig('correlation_heatmap.png')
    plt.show()

    cleaned_data.to_csv('cleaned_healthcare_dataset.csv', index=False)
    print("Cleaned data saved to 'cleaned_healthcare_dataset.csv'")
