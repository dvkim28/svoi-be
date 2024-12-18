from django.urls import path

from advr.views import CategoryViewSet, SubCategoryViewSet

urlpatterns = [
    path(
        "<slug:slug>/",
        CategoryViewSet.as_view({'get': 'retrieve'}),
        name="category-detail",
    ),
    path(
        "<slug:category_slug>/<slug:slug>/",
        SubCategoryViewSet.as_view({'get': 'retrieve'}),
        name="subcategory-detail",
    ),
]
