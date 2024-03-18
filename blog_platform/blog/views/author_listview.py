from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from blog.models import Author
from blog.serializers import AuthorSerializer

class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["first_name", "last_name"]