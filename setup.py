from setuptools import setup, find_packages
from pathlib import Path

# Lee requirements.txt con codificación UTF-8
requirements = (Path(__file__).parent / 'requirements.txt').read_text(encoding="utf-8").splitlines()

# Lee README.md con codificación UTF-8
readme = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")

setup(
    name="Análisis de transacciones bancarias",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=requirements,
    python_requires=">=3.10",
    

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