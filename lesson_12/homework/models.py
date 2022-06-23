from sqlalchemy import Integer, Float, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    product_name = Column(String)
    price = Column(Float)
    product_quantity = Column(Integer)
    comment = Column(String)

    purchases = relationship("Purchase", back_populates="product")


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    user_name = Column(String)

    purchases = relationship("Purchase", back_populates="user")


class Purchase(Base):
    __tablename__ = "purchase"
    id = Column(Integer, primary_key=True)
    purchase_quantity = Column(Integer)

    user_id = Column(Integer, ForeignKey("user.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    user = relationship("User", back_populates="purchases")
    product = relationship("Product", back_populates="purchases")
