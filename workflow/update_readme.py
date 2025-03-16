import pandas as pd
import os

# Definir rutas correctas
# Subir un nivel desde ./workflow/
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
csv_path = os.path.join(base_dir, "data.csv")
readme_path = os.path.join(base_dir, "README.md")

# Cargar el CSV
df = pd.read_csv(csv_path)

# Formatear la tabla en Markdown
markdown_table = df.to_markdown(index=False)

# Leer el README
with open(readme_path, "r") as file:
    readme = file.readlines()

# Buscar y reemplazar la sección de la tabla
start = readme.index("<!-- START_TABLE -->\n") + 1
end = readme.index("<!-- END_TABLE -->\n")
readme[start:end] = [markdown_table + "\n"]

# Guardar cambios
with open(readme_path, "w") as file:
    file.writelines(readme)

print("README actualizado con los datos de data.csv")
