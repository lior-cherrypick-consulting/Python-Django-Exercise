from django_filters import rest_framework as filters
from blog.models import Author


class AuthorFilter(filters.FilterSet):
    first_name = filters.CharFilter(field_name="first_name", lookup_expr="icontains")
    last_name = filters.CharFilter(field_name="last_name", lookup_expr="icontains")

    class Meta:
        model = Author
        fields = ["first_name", "last_name"]
