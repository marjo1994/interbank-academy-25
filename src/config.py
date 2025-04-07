from pathlib import Path
import sys

# Definición de rutas base
PROJECT_ROOT = Path(__file__).parent.parent
INPUT_DIR = PROJECT_ROOT / "input"
OUTPUT_DIR = PROJECT_ROOT / "output"

# Creación de directorio con manejo de errores
try:
    OUTPUT_DIR.mkdir(exist_ok=True)
except PermissionError:
    print(f"Error: No hay permisos para crear {OUTPUT_DIR}", file=sys.stderr)
    sys.exit(1)