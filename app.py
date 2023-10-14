import pandas as pd
import numpy as np
import streamlit as st

# Crear datos de ejemplo
marcas = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan', 'BMW', 'Mercedes-Benz', 'Audi', 'Volkswagen', 'Hyundai']
modelos = ['Camry', 'Civic', 'F-150', 'Silverado', 'Altima', 'X5', 'C-Class', 'A4', 'Jetta', 'Elantra']
anios = [2018, 2020, 2019, 2017, 2016, 2021, 2018, 2020, 2019, 2017]
precios = np.random.randint(15000, 50000, 10)

# Crear DataFrame con los datos
df_autos = pd.DataFrame({'marca': marcas, 'modelo': modelos, 'anio': anios, 'precio': precios})

# Mostrar el DataFrame
print(df_autos)

#eJRCICIOS LOC
#1
st.header("Ejercicio 1 LOC")
st.write("Seleccionar todas las filas de la columna Marca")
df_autos.loc[:, 'marca']

#2
st.header("Ejercicio 2 LOC")
st.write("Seleccionar las filas de los autos cuyo precio es mayor a $40,000")
ej2= df_autos.loc[df_autos["precio"] > 40000]
st.dataframe(ej2)

#3
st.header("Ejercicio 3 LOC")
st.write("Seleccionar las filas de los autos que son de la marca BMW")
ej3= df_autos.loc[df_autos["marca"] == "BMW"]
st.dataframe(ej3)

#4
st.header("Ejercicio 4 LOC")
st.write("Seleccionar las filas de los autos que son de la marca Toyota y tienen un precio menor a $20,000.")
ej4=df_autos.loc[(df_autos["marca"]=="Toyota") & (df_autos["precio"] < 20000)]
st.dataframe(ej4)

#5
st.header("Ejercicio 5 LOC")
st.write("Seleccionar las filas de los autos que son del año 2019.")
ej5=df_autos.loc[df_autos["anio"]== 2019]
st.dataframe(ej5)

#6
st.header("Ejercicio 6 LOC")
st.write("Seleccionar las filas de los autos que son del año 2016 o anteriores.")
ej6=df_autos.loc[df_autos["anio"]<=2016]
st.dataframe(ej6)

#7
st.header("Ejercicio 7 LOC")
st.write("Seleccionar las filas de los autos que son de la marca Honda y el modelo es Civic.")
ej7=df_autos.loc[(df_autos["marca"]=="Honda") & (df_autos["modelo"] == "Civic")]
st.dataframe(ej7)

#8
st.header("Ejercicio 8 LOC")
st.write("Seleccionar las filas de los autos que tienen un precio entre $25,000 y $30,000.")
ej8=df_autos.loc[(df_autos["precio"]>25000) & (df_autos["precio"]<=30000)]
st.dataframe(ej8)

#9
st.header("Ejercicio 9 LOC")
st.write("Seleccionar las filas de los autos que tienen un precio mayor a $30,000 y el modelo es C-Class")
ej9=df_autos.loc[(df_autos["precio"]>30000) & (df_autos["modelo"]=='C-Class')]
st.dataframe(ej9)

#10
st.header("Ejercicio 10 LOC")
st.write("Seleccionar las filas de los autos que son de la marca Volkswagen y el modelo no es Jetta")
ej10=df_autos.loc[(df_autos["marca"]=='Volkswagen') & (df_autos["modelo"]!='Jetta') ]
st.dataframe(ej10)


#EJERCICIOS ILOC

#1
st.header("Ejercicio 1  ILOC")
st.write("Seleccionar las filas de los autos de los primeros 5 fabricantes en el DataFrame.")
ej1=df_autos.iloc[0:5]
st.dataframe(ej1)

#2
st.header("Ejercicio 2  ILOC")
st.write("Seleccionar las filas de los autos de los últimos 5 fabricantes en el DataFrame.")
ej2=df_autos.iloc[5:]
st.dataframe(ej2)

#3
st.header("Ejercicio 3 ILOC")
st.write("Seleccionar la primera columna de todas las filas del DataFrame.")
ej3=df_autos.iloc[:,0]
st.dataframe(ej3)

#4
st.header("Ejercicio 4 ILOC")
st.write("Seleccionar las celdas de la primera fila y primera columna del DataFrame")
ej4=df_autos.iloc[0:1,0]
st.dataframe(ej4)

#5
st.header("Ejercicio 5 ILOC")
st.write("Seleccionar las filas pares del DataFrame.")
ej5=df_autos.iloc[::2]
st.dataframe(ej5)

#6
st.header("Ejercicio 6 ILOC")
st.write("Seleccionar las filas impares del DataFrame que tienen un precio mayor a $25,000.")
ej6=df_autos.iloc[1::2][df_autos['precio']>25000]
st.dataframe(ej6)

#7
st.header("Ejercicio 7 ILOC")
st.write("Seleccionar las filas de los autos que son de la marca Ford y el modelo es F-150")
ej7=df_autos.iloc[:][df_autos["marca"]=='Ford'][df_autos["modelo"]=='F-150']
st.dataframe(ej7)

#8
st.header("Ejercicio 8 ILOC")
st.write("Seleccionar las filas de los autos que son del año 2018 y tienen un precio mayor a $20,000.")
ej8=df_autos.iloc[:][df_autos["anio"]== 2018][df_autos["precio"]>20000]
st.dataframe(ej8)

#9
st.header("Ejercicio 9 ILOC")
st.write("Seleccionar las filas de los autos que tienen un precio mayor a $30,000 y la marca es Toyota")
ej9=df_autos.iloc[:][df_autos["precio"]>30000][df_autos["marca"]=='Toyota']
st.dataframe(ej9)

#10
st.header("Ejercicio 10 ILOC")
st.write("Seleccionar las filas de los autos que son de la marca Honda y el modelo no es Civic")
ej10=df_autos.iloc[:][df_autos["marca"]=='Honda'][df_autos["modelo"]=='Civic']
st.dataframe(ej10)