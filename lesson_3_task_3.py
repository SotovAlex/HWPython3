from address import Address

from mailing import Mailing

to_address = Address("15478", "Москва", "Проспект Ленина", "10", "24")
from_address = Address ("196548", "Нижний Новгород", "проспект Кирова", "15", "48")
mail = Mailing(250, "1585", to_address, from_address )

print (mail)