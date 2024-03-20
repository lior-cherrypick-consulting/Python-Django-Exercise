# blog/tests/test_views.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from blog.models import Author, Category, Post
from datetime import date

class AuthorListViewTest(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.author = Author.objects.create(first_name='John', last_name='Doe')

    def test_author_list(self):
        url = reverse('author-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_author_filter(self):
        url = reverse('author-list') + '?first_name=John'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

class CategoryListViewTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name='Technology')

    def test_category_list(self):
        url = reverse('category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_category_filter(self):
        url = reverse('category-list') + '?name=Technology'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

class PostListViewTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.author = Author.objects.create(first_name='Joe', last_name='Doe')
        cls.category = Category.objects.create(name='Technology')
        cls.post = Post.objects.create(
            title='Sample Post',
            content='Some content',
            author=cls.author,
            category=cls.category,
            created_at=date.today()
        )

    def test_post_list(self):
        url = reverse('post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_post_filter_title(self):
        url = reverse('post-list') + '?title=Sample Post'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
    def test_post_filter_author(self):
        url = reverse('post-list') + '?author=Joe'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
    def test_post_filter_category(self):
        url = reverse('post-list') + '?category=Technology'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
    def test_post_filter_created_at(self):
        url = reverse('post-list') + f'?date={date.today()}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
