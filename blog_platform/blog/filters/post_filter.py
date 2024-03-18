from django_filters import rest_framework as filters, DateFilter
from blog.models import Post


class PostFilter(filters.FilterSet):
    author = filters.CharFilter(
        field_name="author__first_name", lookup_expr="icontains"
    )
    category = filters.CharFilter(field_name="category__name", lookup_expr="icontains")
    created_at = DateFilter(field_name="created_at", lookup_expr="exact")

    class Meta:
        model = Post
        fields = ["title", "author", "category", "created_at"]
