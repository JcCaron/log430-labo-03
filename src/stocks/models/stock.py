"""
Product stock class (value object)
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orders.models.base import Base

class Stock(Base):
    __tablename__ = 'stocks'
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True, nullable=False)
    quantity = Column(Integer, nullable=False)
    
    product = relationship("Product", back_populates="stocks")