from rest_framework import mixins
from rest_framework.exceptions import NotFound
from rest_framework.viewsets import GenericViewSet
from advr.models import Category, SubCategory, Ad
from advr.serializers import (
    CategorySerializer,
    SubCategorySerializer,
    AdSerializer
)
from django.shortcuts import get_object_or_404


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
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    lookup_field = "slug"

    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        return SubCategory.objects.filter(category__slug=category_slug)


class AdViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    lookup_field = "slug"

    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        sub_category_slug = self.kwargs.get("sub_category_slug")
        return Ad.objects.filter(
            sub_category__slug=sub_category_slug,
            sub_category__category__slug=category_slug
        )
