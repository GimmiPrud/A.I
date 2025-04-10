
import pandas as pd

DataTitanic = pd.read_csv("..dati/TitanicData.csv")
print(DataTitanic.tail(7))
print("\n")

ages = DataTitanic["Age"]
print(ages.describe())
print("\n")


