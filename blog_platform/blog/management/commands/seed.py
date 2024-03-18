from django.core.management.base import BaseCommand
from blog.models import Author, Category, Post
from django.utils.text import slugify
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = "Populate the database with fake data"

    def handle(self, *args, **options):
        # Create 20 authors
        authors = [
            Author(first_name=fake.first_name(), last_name=fake.last_name())
            for _ in range(20)
        ]
        Author.objects.bulk_create(authors)

        # Create 10 categories
        categories = [
            Category(name="Technology"),
            Category(name="Lifestyle"),
            Category(name="Entertainment"),
            Category(name="Travel"),
            Category(name="Culinary"),
            Category(name="Wellness"),
            Category(name="Business"),
            Category(name="Finance"),
            Category(name="Education"),
            Category(name="News"),
        ]
        Category.objects.bulk_create(categories)

        # Get created authors and categories
        authors = list(Author.objects.all())
        categories = list(Category.objects.all())

        # Create 10,000 blog posts
        posts = [
            Post(
                title=fake.sentence(),
                content="\n".join(fake.paragraphs()),
                author=fake.random_element(authors),
                category=fake.random_element(
                    categories
                ),  # Assign a category to each post
                created_at=fake.date_between(start_date="-10y", end_date="today"),
            )
            for _ in range(10_000)
        ]
        Post.objects.bulk_create(posts)

        self.stdout.write(
            self.style.SUCCESS(f"Successfully populated the database with fake data")
        )
