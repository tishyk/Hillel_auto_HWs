from models import AddressModel
from session import session
from sqlalchemy import text


class AddressRepository:
    def __init__(self):
        self.__session = session
        self.__model = AddressModel



    def get_all_sql(self):
        query = text("SELECT * FROM addresses")
        addresses = self.__session.execute(query)
        return addresses.all()

    def get_all(self):
        addresses = self.__session.query(self.__model).all()
        return addresses

    def get_by_id(self, address_id: int) -> AddressModel:
        address: AddressModel | None = self.__session.get(self.__model, {'address_id': address_id})
        return address

    def create_new(self, address_modal: AddressModel) -> bool:
        try:
            self.__session.add(address_modal)
            return True
        except:
            return False

    def delete_by_id(self, address_id: int) -> bool:
        try:
            address = self.get_by_id(address_id)
            self.__session.delete(address)
            return True
        except:
            return False

    def update(self, address_model: AddressModel):
        self.__session.query(self.__model)\
         .filter(self.__model.address_id == address_model.address_id)\
         .update({AddressModel.city: address_model.city, AddressModel.country: address_model.country})


repo = AddressRepository()
print(repo.get_all())
print(repo.get_all_sql())
print(repo.get_by_id(1))
# ternopil = AddressModal()
# ternopil.country = "Ukraine"
# ternopil.city = "Ternopil"
# repo.create_new(ternopil)
# repo.delete_by_id(5)
# print(repo.get_all())

# lviv = repo.get_by_id(7)
# lviv.city = "Lviv"
# repo.update(lviv)
print(repo.get_all())
for a in repo.get_all():
    print(a)
    print("a")