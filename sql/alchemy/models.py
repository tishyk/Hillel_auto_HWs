from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from session import engine
from sqlalchemy import Table, Column, Integer, String, MetaData

Base = declarative_base()


class AddressModel(Base):
    __tablename__ = 'addresses'
    address_id = Column(INTEGER, primary_key= True)
    city = Column(VARCHAR(300))
    country = Column(VARCHAR(300))
    users = relationship("UserModel", back_populates='address')

    def __str__(self):
        return f"Id: {self.address_id}, City: {self.city}, Country: {self.country}, Users: {self.users}"

    def __repr__(self):
        return f"Id - {self.address_id} City - {self.city} Country - {self.country}, Users: {self.users}"

class UserModel(Base):
    __tablename__ = "users"
    user_id = Column(INTEGER, primary_key=True)
    email = Column(VARCHAR(100))
    password = Column(VARCHAR(100))
    age = Column(INTEGER)
    address_id = Column(ForeignKey("addresses.address_id"))
    address = relationship("AddressModel", back_populates="users")

    def __repr__(self):
        return f"Id - {self.user_id} Age - {self.age} Email - {self.email}"


    def __str__(self):
        return f"Id - {self.user_id} Age - {self.age} Email - {self.email}"


meta = MetaData()

students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('lastname123', String),
    )

meta.create_all(engine)


