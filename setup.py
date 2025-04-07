from setuptools import setup, find_packages
from pathlib import Path

# Lee requirements.txt
requirements = (Path(__file__).parent / 'requirements.txt').read_text().splitlines()

# Lee README para la descripción larga
readme = (Path(__file__).parent / "README.md").read_text()

setup(
    name="Análisis de transacciones bancarias",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=requirements,
    python_requires=">=3.10",
    
    # Archivos de datos (incluye input si es necesario)
    package_data={
        "": ["*.csv", "*.txt"],  # Patrones de archivos a incluir
    },
    
    # Scripts ejecutables
    entry_points={
        "console_scripts": [
            "interbank-transacciones=cli:main",
        ],
    },
    
    # Metadata adicional
    author="Marjorie Herrera Lengua",
    description="Procesamiento de transacciones bancarias",
    long_description=readme,
    long_description_content_type="text/markdown",
)