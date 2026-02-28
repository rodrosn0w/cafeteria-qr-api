from sqlalchemy import Column, Integer, String, Boolean, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

# 1. Modelo de la Mesa
class Table(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True, index=True)    
    number = Column(String(50), nullable=False)
    qr_code_token = Column(String(100), unique=True, index=True)
    is_active = Column(Boolean, default=True)

    # Relación: Una mesa puede tener muchos pedidos
    orders = relationship("Order", back_populates="table")


# 2. Modelo del Producto
class Product(Base):
    __tablename__ = "product" # Usamos el nombre en singular tal como lo creaste

    id = Column(Integer, primary_key=True, index=True)    
    name = Column(String(100), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    category = Column(String(50), nullable=False) # MySQL validará el ENUM por nosotros
    stock_status = Column(Boolean, default=True)


# 3. Modelo del Pedido (Cabecera)
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    table_id = Column(Integer, ForeignKey("tables.id"))
    total = Column(Numeric(10, 2), default=0.00)
    status = Column(String(20), default="pending") 
    payment_method = Column(String(20), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relaciones
    table = relationship("Table", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")


# 4. Modelo del Detalle del Pedido (Los productos que pidió)
class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"))
    product_id = Column(Integer, ForeignKey("product.id"))
    quantity = Column(Integer, nullable=False)
    subtotal = Column(Numeric(10, 2))

    # Relaciones
    order = relationship("Order", back_populates="items")
    product = relationship("Product")