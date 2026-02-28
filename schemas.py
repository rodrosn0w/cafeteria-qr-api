from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime
from decimal import Decimal

# --- ESQUEMAS PARA PRODUCTOS ---
# Lo que devolvemos cuando el frontend pida el menú
class ProductResponse(BaseModel):
    id: int
    name: str
    price: Decimal
    category: str
    stock_status: bool

    model_config = ConfigDict(from_attributes=True)

# --- ESQUEMAS PARA EL DETALLE DEL PEDIDO ---
# Lo que envía el cliente desde su celular
class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int

# Lo que devolvemos al leer un pedido
class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    subtotal: Decimal

    model_config = ConfigDict(from_attributes=True)

# --- ESQUEMAS PARA EL PEDIDO COMPLETO (ORDERS) ---
# El JSON completo que envía el QR para hacer un pedido nuevo
class OrderCreate(BaseModel):
    table_id: int
    payment_method: str
    items: List[OrderItemCreate] # Lista de los productos que quiere

# La respuesta completa con el estado y el total calculado
class OrderResponse(BaseModel):
    id: int
    table_id: int
    total: Decimal
    status: str
    payment_method: str
    created_at: datetime
    items: List[OrderItemResponse]

    model_config = ConfigDict(from_attributes=True)