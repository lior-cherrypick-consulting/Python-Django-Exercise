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
            Category(name="Food & Drink"),
            Category(name="Health & Wellness"),
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
        posts = []
        for _ in range(10000):
            author = fake.random_element(authors)
            post = Post(
                title=fake.sentence(),
                content="\n".join(fake.paragraphs()),
                author=author,
            )
            post.save()  # save to get a post instance to add categories
            post.categories.add(*fake.random_elements(elements=categories, unique=True))
            posts.append(post)

        self.stdout.write(
            self.style.SUCCESS(f"Successfully populated the database with fake data")
        )
