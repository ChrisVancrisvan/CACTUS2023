import pandas as pd
import matplotlib.pyplot as plt
import folium

# Obtener datos
datos_accidentes = pd.read_csv('incidentesviales_noviembre22.csv')  # Reemplaza 'datos_accidentes.csv' con el nombre de tu archivo de datos

# Analizar datos
calles_peligrosas = datos_accidentes['calle'].value_counts().head(10)  # Obtén las 10 calles con más accidentes

# Visualización de datos - Gráfico de barras
plt.bar(calles_peligrosas.index, calles_peligrosas.values)
plt.xlabel('Calle')
plt.ylabel('Número de accidentes')
plt.title('Las calles más peligrosas en Monterey')
plt.xticks(rotation=45)
plt.show()

# Visualización de datos - Mapa interactivo
mapa = folium.Map(location=[36.6002, -121.8947], zoom_start=12)  # Coordenadas de Monterey
for index, row in datos_accidentes.iterrows():
    folium.Marker([row['latitud'], row['longitud']], popup=row['calle']).add_to(mapa)
mapa.save('mapa.html')
