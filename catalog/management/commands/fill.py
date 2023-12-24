from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'name': 'Категория 8', 'description': 'Категория 8, добавленная кастомной командой'},
            {'name': 'Категория 9', 'description': 'Категория 9, добавленная кастомной командой'},
            {'name': 'Категория 10', 'description': 'Категория 10, добавленная кастомной командой'},
            {'name': 'Категория 11', 'description': 'Категория 11, добавленная кастомной командой'},
        ]

        categories_for_create = []
        for category in category_list:
            categories_for_create.append(
                Category(**category)
            )

        Category.objects.all().delete()
        Category.objects.bulk_create(categories_for_create)