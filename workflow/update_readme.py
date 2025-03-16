import pandas as pd
import os
import math
from datetime import datetime

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
csv_path = os.path.join(base_dir, "data.csv")
readme_path = os.path.join(base_dir, "README.md")

df = pd.read_csv(csv_path)

coverage_columns = df.columns[1:]

def convert_to_numeric(value):
    weights = {
        "Basic": 25,
        "Medium": 50,
        "Full": 100
    }
    return weights.get(value, 0)

df_numeric = df.copy()
for col in coverage_columns:
    df_numeric[col] = df[col].map(convert_to_numeric)

df["% Coverage"] = df_numeric[coverage_columns].mean(axis=1)

df["% Coverage"] = df["% Coverage"].apply(lambda x: f'![](https://geps.dev/progress/{math.floor(x)})')

total_coverage = math.floor(df_numeric[coverage_columns].mean().mean())

current_date = datetime.now().strftime("%d/%m/%Y")

markdown_table = df.to_markdown(index=False, tablefmt="github")

readme_content = f"""### Cobertura de pruebas en la API

{markdown_table}

Cobertura total  
![](https://geps.dev/progress/{total_coverage})

Última actualización {current_date}
"""

with open(readme_path, "w") as file:
    file.write(readme_content)

print("README actualizado con los datos de data.csv")
