#Colas
import pandas as pd
#read_file= pd.read_excel(r'C:/Users/Nobody 3/Desktop/BSDD.xlsx')
#read_file.to_csv(r'C:/Users/Nobody 3/Desktop/BSDD.csv')

mi_excel = pd.read_excel('Base de datos.xlsx')
print(mi_excel)

with open('C:/Users/Nobody 3/PycharmProjects/Vector1/PROYECTO/Base de datos.csv', encoding='utf-8') as archivo:
    cola = archivo.read().splitlines()

print("\t")

#Sacar usuarios del inicio
u= cola.pop(1)
print(f"Facilitando préstamo a {u}")
u=cola.pop(1)
print(f"Facilitando préstamo a {u}")
u=cola.pop(1)
print(f"Facilitando préstamo a {u}")
u=cola.pop(1)
print(f"Facilitando préstamo a {u}")
u=cola.pop(1)
print(f"Facilitando préstamo a {u}")


