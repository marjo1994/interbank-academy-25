from pydantic import BaseModel, Field, field_validator, ConfigDict
from enum import Enum

# Definir un Enum para los tipos de transacción, solo permite "Crédito" o "Débito".
class TipoTransaccion(str, Enum):
    CREDITO = "Crédito"
    DEBITO = "Débito"

    # Mensaje personalizado cuando se ingresa un valor no permitido
    def __str__(self):
       return f"Los valores permitidos son: {', '.join([e.value for e in cls])}"

# Modelo para cada transacción
class Transaccion(BaseModel):
    id: int                  # Debe ser un entero
    tipo: TipoTransaccion    # Solo permite los valores del Enum
    monto: float = Field(..., gt=0) # El monto es un campo requerido y debe ser mayor a 0.

    # Usando Field Validator podemos mostrar un mensaje claro y específico cuando el monto excede a s/.1,000,000.
    @field_validator('monto')
    def validar_monto(cls, valor):
        if valor > 1_000_000:
            raise ValueError("El monto no puede exceder S/1,000,000")
        return round(valor, 2)


# Modelo para el reporte final, puesto que asegura que los cálculos sean correctos y que los sistemas que consuman el reporte no fallen.
class MaxTransaccion(BaseModel):
    id: int
    monto: float

class ConteoTransacciones(BaseModel):
    model_config = ConfigDict(populate_by_name=True)  # Permite usar alias al crear objetos
    credito: int = Field(..., alias="Crédito", ge=0)
    debito: int = Field(..., alias="Débito", ge=0)

class ReporteTransaccion(BaseModel):
    balance_final: float
    max_transaccion: MaxTransaccion
    conteo_transacciones: ConteoTransacciones