from django.urls import path
from .views import AuthorListView, CategoryListView, PostListView

urlpatterns = [
    path("author/", AuthorListView.as_view(), name="author-list"),
    path("category/", CategoryListView.as_view(), name="category-list"),
    path("post/", PostListView.as_view(), name="post-list"),
]
