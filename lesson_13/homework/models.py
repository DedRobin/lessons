from sqlalchemy import Integer, Float, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)

    # links from tables
    profile = relationship("Profile", back_populates="user")  # link from table <-- "Profile"
    addresses = relationship("Address", back_populates="user")  # link from table <-- "Address"
    purchases = relationship("Purchase", back_populates="user")  # link from table <-- "Purchase"

    # def __repr__(self):
    #     return f"{self.id}, {self.email}, {self.password}"

class Profile(Base):
    __tablename__ = "profile"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    age = Column(Integer)

    # foreign key
    user_id = Column(Integer, ForeignKey("user.id"))

    # links to tables
    user = relationship("User", back_populates="profile")  # link to table --> "User"

    # def __repr__(self):
    #     return f"{self.id}, {self.name}, {self.phone}, {self.age}"

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    city = Column(String)
    address = Column(String)

    # foreign key
    user_id = Column(Integer, ForeignKey("user.id"))

    # links ro tables
    user = relationship("User", back_populates="addresses")  # link to table --> "User"

    # def __repr__(self):
    #     return f"{self.id}, {self.city}, {self.address}"


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    product_name = Column(String)
    price = Column(Float)
    product_quantity = Column(Integer)
    comment = Column(String)

    # links from tables
    purchases = relationship("Purchase", back_populates="product")  # link from table --> "Purchase"

    # def __repr__(self):
    #     return f"{self.id}, {self.product_name}, {self.price}, {self.product_quantity}, {self.comment}"


class Purchase(Base):
    __tablename__ = "purchase"
    id = Column(Integer, primary_key=True)
    purchase_quantity = Column(Integer)

    # foreign keys
    user_id = Column(Integer, ForeignKey("user.id"))
    product_id = Column(Integer, ForeignKey("product.id"))

    # links to tables
    user = relationship("User", back_populates="purchases")  # link to table --> "User"
    product = relationship("Product", back_populates="purchases")  # link to table --> "Product"

    # def __repr__(self):
    #     return f"{self.id}, {self.purchase_quantity}"

