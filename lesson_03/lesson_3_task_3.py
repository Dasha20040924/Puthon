from address import Address
from mailing import Mailing

to_addr = Address(
    index="123456",
    city="Москва",
    street="Ленинский проспект",
    house="10",
    apartment="15"
)

from_addr = Address(
    index="654321",
    city="Санкт-Петербург",
    street="Невский проспект",
    house="20",
    apartment="30"
)

mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=250,
    track="AB123456789RU"
)

print(
      f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - "
      f"{mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей."
      )
