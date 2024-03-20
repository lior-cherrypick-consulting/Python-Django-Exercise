from django.test import TestCase
from blog.models import Author, Category, Post
from datetime import date

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = Author.objects.create(first_name='John', last_name='Doe')

    def test_author_str(self):
        self.assertEqual(str(self.author), self.author.first_name + " " + self.author.last_name)

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name='Technology')

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Technology')

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = Author.objects.create(first_name='Jane', last_name='Smith')
        cls.category = Category.objects.create(name='Lifestyle')
        cls.post = Post.objects.create(
            title='Sample Post Title',
            content='Sample post content.',
            author=cls.author,
            category=cls.category,
            created_at=date.today()
        )

    def test_post_str(self):
        self.assertEqual(str(self.post), 'Sample Post Title')

    def test_post_author(self):
        self.assertEqual(self.post.author, self.author)

    def test_post_category(self):
        self.assertEqual(self.post.category, self.category)

    def test_post_created_at(self):
        self.assertEqual(self.post.created_at, date.today())
