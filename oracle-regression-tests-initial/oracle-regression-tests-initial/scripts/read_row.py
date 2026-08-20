import pandas as pd

# Wczytaj plik CSV
df = pd.read_csv('testsets.csv')

# Wypisz pierwszy wiersz
print(df.iloc[0])