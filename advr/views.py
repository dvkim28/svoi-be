from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import GenericViewSet

from advr.models import Category, SubCategory, Ad
from advr.serializers import (
    CategorySerializer,
    SubCategorySerializer,
    AdSerializer
)


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
        sub_category_slug = self.kwargs.get("sub_category_slug")
        return get_object_or_404(
            queryset,
            category__slug=category_slug,
            slug=sub_category_slug
        )


class AdViewSet(
    GenericViewSet,
    mixins.RetrieveModelMixin,
):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def get_object(self):
        queryset = self.get_queryset()
        category_slug = self.kwargs.get("category_slug")
        sub_category_slug = self.kwargs.get("sub_category_slug")
        ad_slug = self.kwargs.get("ad_slug")
        return get_object_or_404(
            queryset,
            sub_category__slug=sub_category_slug,
            sub_category__category__slug=category_slug,
            slug=ad_slug
        )
