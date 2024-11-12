# %%
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

# Cargar el archivo Excel
demanda_diaria_df = pd.read_excel(r'C:\Users\Lucas\VisualCode\Python\GraficosPanaderia\Graficos\Demanda ingredientes diaria.xlsx', sheet_name='DemandaDiaria')
ingredientes_df = pd.read_excel(r'C:\Users\Lucas\VisualCode\Python\GraficosPanaderia\Graficos\Demanda ingredientes diaria.xlsx', sheet_name='Ingredientes')
demanda_ingredientes_df = pd.read_excel(r'C:\Users\Lucas\VisualCode\Python\GraficosPanaderia\Graficos\Demanda ingredientes diaria.xlsx', sheet_name='DemandaIngredientes')

# Establecer la primera columna como índice para que los productos queden como nombres de filas
demanda_diaria_df.set_index(demanda_diaria_df.columns[0], inplace=True)

# Transponer el DataFrame para que los días estén en las filas y los productos en las columnas
df = demanda_diaria_df.transpose()

# Convertir los valores de la tabla a numéricos (si es necesario)
df = df.apply(pd.to_numeric, errors='coerce')

# Verificar los datos (solo para confirmar)
print(df.head())

# Seleccionar solo hasta el día 357
df_limited = df.iloc[:357]

# Crear gráficos por cada producto
for product in df_limited.columns:
    plt.figure(figsize=(10, 5))  # Ajustar el tamaño del gráfico
    plt.plot(df_limited.index, df_limited[product], label=product, color='blue')
    
    # Personalización del gráfico
    plt.title(f'Demanda de {product} a lo largo de los Días', fontsize=14)
    plt.xlabel('Días', fontsize=12)
    plt.ylabel('Demanda', fontsize=12)
    plt.grid(True)
    plt.xticks(rotation=45, fontsize=10)
    plt.yticks(fontsize=10)
    plt.legend()
    plt.tight_layout()  # Ajustar el diseño para que no se corten las etiquetas

    # Mostrar el gráfico
    plt.show()

## Instalar jupyter
# %%
