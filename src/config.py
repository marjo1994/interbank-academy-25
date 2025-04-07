from pathlib import Path
import sys

# Configuración básica de rutas
PROJECT_ROOT = Path(__file__).parent.parent  # Raíz del proyecto
INPUT_DIR = PROJECT_ROOT / "input"           # Carpeta de entrada
OUTPUT_DIR = PROJECT_ROOT / "output"         # Carpeta de salida

# Creación de directorio con manejo de errores
try:
    OUTPUT_DIR.mkdir(exist_ok=True)
except PermissionError:
    print(f"Error: No hay permisos para crear {OUTPUT_DIR}", file=sys.stderr)
    sys.exit(1)