from django.core.management.base import BaseCommand
from Shop.models import Unit, Category, Contact

class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        categories = [
            {'name': 'Troops',
             'description': 'Основные боевые подразделения любой армии'},
            {'name': 'HQ',
             'description': 'Командиры армий'},
            {'name': 'Heavy Support',
             'description': 'Отряды тяжелой огневой поддержки'},
            {'name': 'Elite',
             'description': 'Элитные подразделения армий'},
            {'name': 'Fast Attack',
             'description': 'Отряды мобильных войск'},
        ]

        units = [
            {'name': 'Tactical Squad', 'category': 'Troops',
             'description': 'Отряды тактических десантников - это основа любого ордена комодесанта. Войны, способоные выполнять любые боевые задачи на поле боя, максимально подстраиваясь под условия боя.'},
            {'name': 'Scout Squad', 'category': 'Troops',
             'description': 'Скауты являютя молодыми бойцами, которые еще только претендуют на честь стать полноправным братом своего ордена. Под руководством опытного сержата они идут в разведку, чтобы предоставить данные о позициях противника и боевой обстановке.'},
        ]

        Category.objects.all().delete()
        for category in categories:
            new_category = Category(**category)
            new_category.save()

        Unit.objects.all().delete()
        for unit in units:
            category_name = unit['category']
            category = Category.objects.get(name=category_name)
            unit['category'] = category
            new_unit = Unit(**unit)
            new_unit.save()

        contacts = [
            {'full_name': 'Dmitry'},
            {'full_name': 'Kravets'},
            {'full_name': 'Dmitry'},
            {'full_name': 'Kravets'},
            {'full_name': 'Dmitry'},
            {'full_name': 'Kravets'},
            {'full_name': 'Dmitry'},
            {'full_name': 'Kravets'},
            {'full_name': 'Dmitry'},
            {'full_name': 'Kravets'},
            {'full_name': 'Dmitry'},
            {'full_name': 'Kravets'},{'full_name': 'Dmitry'},
            {'full_name': 'Kravets'},
            {'full_name': 'Dmitry'},
            {'full_name': 'Kravets'},
            {'full_name': 'Dmitry'},
            {'full_name': 'Kravets'},
            {'full_name': 'Dmitry'},
            {'full_name': 'Kravets'},
            {'full_name': 'Dmitry'},
            {'full_name': 'Kravets'},{'full_name': 'Dmitry'},
            {'full_name': 'Kravets'},{'full_name': 'Dmitry'},
            {'full_name': 'Kravets'},
            {'full_name': 'Dmitry'},
            {'full_name': 'Kravets'},
            {'full_name': 'Dmitry'},
            {'full_name': 'Kravets'},
            {'full_name': 'Dmitry'},
            {'full_name': 'Kravets'},





        ]

        Contact.objects.all().delete()
        for contact in contacts:
            new_contact = Contact(**contact)
            new_contact.save()