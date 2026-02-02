import pandas as pd

data = {
    "name": ["GigaTolik", "DushnilaVlad", "MaxNa", "RulMusorCat", "SuperMario", "LazyIvan", "CyberAnna", "NoobMaster", "SpeedyGonzales", "JustElena"],
    "group": ["A", "B", "A", "B", "A", "B", "A", "B", "A", "B"],
    "math": [95, 100, 45, 88, 70, None, 92, 30, 75, 85],
    "python": [90, 100, 50, None, 65, 40, 95, 25, 80, 85],
    "hours": [15, 40, 2, 12, 8, 1, 20, 5, 10, 14],
    "passed": [True, True, False, True, True, False, True, False, True, True],
    "city": ["Moscow", "SPb", "Kazan", "Omsk", "Moscow", "Samara", "Novosibirsk", "Ekb", "Sochi", "Moscow"]
}

df = pd.DataFrame(data)

print(df.head(), "\n",
      df.info(), "\n",
      df.describe(), sep="")

print(df[['name', 'group', 'python']])

print(df.iloc[0], "\n",
      df.iloc[2:6], sep="")

df2 = df.set_index('name')
print(df2.loc['GigaTolik'])

top_python = df[df['python'] >= 80]
print(len(top_python))

a_good_math = df[(df['group'] == 'A') & (df['math'] >= 70)]
print(len(a_good_math))

with_missing = df[df['math'].isna() | df['python'].isna()]
print(with_missing)

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

passed_percent = df.groupby('group')['passed'].mean() * 100
print(passed_percent)

rating = df.sort_values(by='avg_score', ascending=False)

cols_to_show = ['name', 'group', 'avg_score', 'level', 'hours', 'passed']
final_view = rating[cols_to_show].head(5)

print(final_view)