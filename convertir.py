import json
import yaml

# 1. Leer el archivo datos.json original
with open('datos.json', 'r') as f:
    datos = json.load(f)

# 2. Agregar el nuevo puerto (4) a la lista
if 4 not in datos['puertos']:
    datos['puertos'].append(4)

# 3. Guardar la configuración actualizada en datos_modificado.json
with open('datos_modificado.json', 'w') as f:
    json.dump(datos, f, indent=4)

# 4. Convertir la estructura y guardarla en datos.yaml
with open('datos.yaml', 'w') as f:
    yaml.dump(datos, f, default_flow_style=False)

print("Archivos creados y válidos: datos_modificado.json y datos.yaml")