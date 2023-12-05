from typing import Any
from django.core.management import BaseCommand
from shop.models import Customer, Product
from random import choice, randint, randrange

NAMES = ['Sharlotta', 'Liza', 'Margo', 'Ahri', 'Jinx', 'Mary']
SURNAMES = ['Black', 'Darkwood', 'Li', 'Tonks']

ITEMS = ['Cheese', 'Milk', 'Cottage cheese', 'Bread', 'Pancake', 'Sausages', 'Sugar',
         'Soju', 'Wine', 'Juice', 'Spoon', 'Fork', 'Socks', 'Shirt', 'T-Shirt',
         'Plate', 'Ramen', 'Soba', 'Pasta', 'Tomato', 'Eggs']


class Command(BaseCommand):
    help = 'Fill DB'

    def handle(self, *args: Any, **options: Any) -> str | None:
        for _ in range(10):
            fullname = f'{choice(NAMES)} {choice(SURNAMES)}'
            customer = Customer(
                name=fullname,
                email=f'{fullname.lower().replace(" ","_")}@mail.com',
                phone_number=f'+7{"".join([str(randint(1,9)) for _ in range(10) ])}',
            )
            customer.save()

        for item in ITEMS:
            product = Product(
                name=item,
                price=randrange(0, 100)/100 + randint(1, 100),
                count=randint(100, 200)
            )
            product.save()
