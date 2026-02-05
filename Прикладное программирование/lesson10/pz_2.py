import pandas as pd
import numpy as np

data = {
    "name": ["Толя", "Влад", "Макс", "Никита", "Марио", "Иван", "Анна", "Егор", "Рома", "Елена", "Руслан", "Михаил", "Ленар", "Витя", "Борис"],
    "group": ["A", "B", "A", "B", "A", "B", "A", "B", "A", "B", "B", "B", "A", "A", "B"],
    "math": [95, 100, 45, 88, 70, 52, 92, 30, 75, 85, 75, 93, 48, 83, 98],
    "python": [90, 100, 50, 85, 65, 40, 95, 25, 80, 85, 65, 86, 35, 90, 80],
    "hours": [15, 40, 2, 12, 8, 1, 20, 5, 10, 14, 20, 15, 5, 40, 12],
    "passed": [True, True, False, True, True, False, True, False, True, True, False, True, True, True, False],
    "city": ["Москва", "Екатеринбург", "Казань", "Омск", "Тула", "Самара", "Новосибирск", "Сочи", "Мурманск", "Якутск", "Владивосток", "Иркутск", "Анапа", "Санкт-Петербург", "Ростов"]
}

df = pd.DataFrame(data)
print('-' * 40)

print(df.head())
print() 
df.info() 
print()
print(df.describe())
print('-' * 40)

print(df[['name', 
          'group', 
          'python']])
print('-' * 40)

print(df.iloc[0], "\n",
      df.iloc[2:6], sep="")
print('-' * 40)

df2 = df.set_index('name')
print(df2.loc['Толя'])
print('-' * 40)

top_python = df[df['python'] >= 80]
print(f"Top Python count: {len(top_python)}")
print('-' * 40)

a_good_math = df[(df['group'] == 'A') & (df['math'] >= 70)]
print(f"Group A good math count: {len(a_good_math)}")
print('-' * 40)

with_missing = df[df['math'].isna() | df['python'].isna()]
print("Rows with missing values:")
print(with_missing)
print('-' * 40)

df['avg_score'] = df[['math', 'python']].mean(axis=1)

def get_level(score):
    if pd.isna(score): return "unknown"
    if score >= 85: return "high"
    elif score >= 70: return "mid"
    else: return "low"

df['level'] = df['avg_score'].apply(get_level)

group_stats = df.groupby('group').agg({
    'avg_score': 'mean',
    'hours': 'mean',
    'name': 'count'
}).rename(columns={'name': 'count'})

print(group_stats)
print('-' * 40)

passed_percent = df.groupby('group')['passed'].mean() * 100
print(passed_percent)
print('-' * 40)

rating = df.sort_values(by='avg_score', ascending=False)

cols_to_show = ['name', 'group', 'avg_score', 'level', 'hours', 'passed']
final_view = rating[cols_to_show].head(5)

print(final_view)
# test 2