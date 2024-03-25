from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import AuthorListView, CategoryListView, PostListView

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("author/", AuthorListView.as_view(), name="author-list"),
    path("category/", CategoryListView.as_view(), name="category-list"),
    path("post/", PostListView.as_view(), name="post-list"),
]
