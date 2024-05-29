import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
data = pd.read_csv('tu_archivo.csv')

# Crear un slider para seleccionar el año
year_to_filter = st.slider('Seleccione el año', min_value=int(data['Year'].min()), max_value=int(data['Year'].max()), value=int(data['Year'].min()))

# Filtrar los datos por el año seleccionado en el slider
filtered_data = data[data['Year'] == year_to_filter]

# Crear un gráfico para el año seleccionado
plt.figure(figsize=(10, 5))
plt.bar(filtered_data['Genre'], filtered_data['Revenue (Millions)'])
plt.title(f'Revenue by Genre in {year_to_filter}')
plt.xlabel('Genre')
plt.ylabel('Revenue (Millions)')
plt.xticks(rotation=45)
plt.tight_layout()

# Mostrar el gráfico en Streamlit
st.pyplot(plt)
