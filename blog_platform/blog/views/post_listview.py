from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from blog.models import Post
from blog.serializers import PostSerializer
from blog.filters import PostFilter


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter
