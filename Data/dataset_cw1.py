import pandas as pd 
import numpy as np

df = pd.read_csv("/home/baguetteking/Desktop/data.csv")
print(df.head())

print("\n")

liczba_probek = df.shape[0]
print(f"Liczba próbek: {liczba_probek}")

print("\n")

print(df.dtypes)

print("\n")

liczba_klas = df['diagnosis'].nunique()
print(f"Liczba klas: {liczba_klas}")

klasy = df['diagnosis'].unique()
print(f"Klasy: {klasy}")