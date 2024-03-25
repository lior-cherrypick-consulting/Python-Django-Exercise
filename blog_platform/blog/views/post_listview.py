from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from blog.models import Post
from blog.serializers import PostSerializer
from blog.filters import PostFilter

class PostListViewPagination(PageNumberPagination):
    page_size = 10

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter
    pagination_class = PostListViewPagination
