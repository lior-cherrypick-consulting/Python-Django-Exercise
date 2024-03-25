from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from blog.models import Author
from blog.serializers import AuthorSerializer
from blog.filters import AuthorFilter


class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AuthorFilter
