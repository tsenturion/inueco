import pandas as pd

print("1.1")
students = [
    {"name": "Alice", "group": "A", "math": 85, "python": 90, "hours": 10, "passed": True, "city": "New York"},
    {"name": "Bob", "group": "B", "math": 78, "python": None, "hours": 8, "passed": True, "city": "Los Angeles"},
    {"name": "Charlie", "group": "A", "math": 92, "python": 88, "hours": 12, "passed": True, "city": "Chicago"},
    {"name": "David", "group": "B", "math": None, "python": 76, "hours": 7, "passed": False, "city": "Houston"},
    {"name": "Eva", "group": "A", "math": 67, "python": 72, "hours": 9, "passed": False, "city": "Phoenix"},
    {"name": "Frank", "group": "B", "math": 80, "python": 85, "hours": 11, "passed": True, "city": "Philadelphia"},
    {"name": "Grace", "group": "A", "math": 95, "python": 93, "hours": 15, "passed": True, "city": "San Antonio"},
    {"name": "Hannah", "group": "B", "math": 60, "python": 65, "hours": 6, "passed": False, "city": "San Diego"},
    {"name": "Ian", "group": "A", "math": 88, "python": 91, "hours": 10, "passed": True, "city": "Dallas"},
    {"name": "Jack", "group": "B", "math": 74, "python": 80, "hours": 8, "passed": True, "city": "San Jose"}
]

print("1.2")
df = pd.DataFrame(students)

print("1.3")
print(df.head())
print(df.info())
print(df.describe())

print("2.1")
print(df[['name', 'group', 'python']])

print("2.2")
print(df.iloc[0])
print(df.iloc[2:6])

print("2.3")
df2 = df.copy()
df2.set_index('name', inplace=True)
print(df2.loc["Eva"])

print("3.1")
top_python = df[df['python'] > 80]
print(top_python)

print("3.2")
a_good_math = df[(df['group'] == 'A') & (df['math'] >= 70)]
print(a_good_math)

print("3.3")
with_missing = df[df[['math', 'python']].isnull().any(axis=1)]
print(with_missing)

print("4.1")
avg_score = df[['math', 'python']].fillna(0).mean(axis=1, skipna=True)
print(avg_score)

print("4.2")
def make_level(avg):
    if avg >= 85:
        return 'high'
    elif 70 <= avg < 85:
        return 'mid'
    else:
        return 'low'
df['avg_score'] = avg_score
df['level'] = df['avg_score'].apply(make_level)
print(df)

print("5.1")
group_stats = df.groupby('group').agg({
    'avg_score': 'mean',
    'hours': 'mean',
    'name': 'count'
})
print(group_stats)

print("5.2")
passed_counts = df.groupby('group')['passed'].mean() * 100
print(passed_counts)

print("6.1")
rating = df.sort_values(by='avg_score', ascending=False)
print(rating)

print("6.2")
final_view = df[['name', 'group', 'avg_score', 'level', 'hours', 'passed']]
print(final_view)