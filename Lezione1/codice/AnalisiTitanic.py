
import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
dataPath = os.path.join(script_dir,'../dati/TitanicData.csv')

print("Dati degli ultimi 7 passegeri del csv sui passeggeri del titainc:\n")
# Lettura file csv
DataTitanic = pd.read_csv(dataPath)
print(DataTitanic.tail(7))
print("----------------")

print("Descrizione sulle età dei passegeri:\n")
ages = DataTitanic["Age"]
print(ages.describe())
print("------------------")


