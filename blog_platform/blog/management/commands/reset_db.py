from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Resets the blog app migrations and optionally drops specific tables'

    def handle(self, *args, **options):
        tables_to_drop = ['blog_author', 'blog_category', 'blog_post', 'django_migrations']
        
        with connection.cursor() as cursor:
            for table in tables_to_drop:
                cursor.execute(f"DROP TABLE IF EXISTS {table} CASCADE;")
                self.stdout.write(self.style.SUCCESS(f'Successfully dropped {table} table.'))