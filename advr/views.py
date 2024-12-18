from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import GenericViewSet

from advr.models import Category, SubCategory
from advr.serializers import CategorySerializer, SubCategorySerializer


class CategoryViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = "slug"


class SubCategoryViewSet(
    GenericViewSet,
    mixins.RetrieveModelMixin,
):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

    def get_object(self):

        queryset = self.get_queryset()
        category_slug = self.kwargs.get("category_slug")
        subcategory_slug = self.kwargs.get("slug")
        return get_object_or_404(
            queryset,
            category__slug=category_slug,
            slug=subcategory_slug
        )
