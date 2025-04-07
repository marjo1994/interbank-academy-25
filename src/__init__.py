"""
Paquete principal para el análisis de transacciones bancarias

Exporta las funciones principales para uso externo
"""

from .cli import main  # Exporta la función principal

__all__ = ['main']  # Controla qué se exporta con 'from src import *'
__version__ = '0.1.0'  # Versión del paquete