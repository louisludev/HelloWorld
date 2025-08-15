import pandas as pd

scores = [
    ['leo', 6, 13, 34, 54],
    ['peter', 10, 53, 44, 67],
    ['equl', 12, 76, 98, 78]
]

df = pd.DataFrame(scores, columns=['name', 'num', 'cn', 'math', 'en'])

df['sum'] = df[['cn', 'math', 'en']].sum(axis=1)
df['avg'] = df[['cn', 'math', 'en']].mean(axis=1).round(1)

print(df)
