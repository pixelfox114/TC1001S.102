import pandas as pd
import calcular



tabla = pd.read_csv('figuras.csv')

for index, row in tabla.iterrows():
    tipo = row.iloc[0]  # first column
    if tipo == "t":
        pass
    elif tipo == "c":
        area, circumference = calcular.circle(row.iloc[1])
        print(f"Circle: area={area}, circumference={circumference}")
    else:
        area, perimeter = calcular.rectangle(   row.iloc[1], row.iloc[2])
        print(f"Rectangle: area={area}, perimeter={perimeter}")
