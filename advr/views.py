from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from advr.models import Category, SubCategory, Ad
from advr.serializers import (
    CategorySerializer,
    SubCategorySerializer,
    AdSerializer, SubCategoryRetrieveSerializers
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
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    lookup_field = "slug"

    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        return SubCategory.objects.filter(category__slug=category_slug)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return SubCategoryRetrieveSerializers
        else:
            return self.serializer_class


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

    def get_serializer_class(self):
        if self.action == "retrieve":
            ad = self.get_object()
            ad.show_count += 1
            ad.save()
            return AdSerializer
