from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from blog.models import Category
from blog.serializers import CategorySerializer
from blog.filters import CategoryFilter


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter
