import pandas as pd

scores = [
    ['Wang', 2, 64, 87, 65],
    ['Chen', 3, 45, 57, 95],
    ['Wu', 4, 55, 89, 28],
    ['Liu', 8, 54, 84, 45],
    ['Lu', 11, 65, 87, 67],
    ['leo', 6, 13, 34, 54],
    ['peter', 10, 53, 44, 67],
    ['equl', 12, 76, 98, 78]
]

df = pd.DataFrame(scores, columns=['Name', 'Num', 'CH', 'Math', 'ENG'])
df['Sum'] = df[['CH', 'Math', 'ENG']].sum(axis=1)
df['Avg'] = df[['CH', 'Math', 'ENG']].mean(axis=1).round(1)

print(df)
