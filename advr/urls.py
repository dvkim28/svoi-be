from django.urls import path
from advr.views import SubCategoryViewSet, AdViewSet, CategoryViewSet

urlpatterns = [
    path(
        "<slug:slug>/",
        CategoryViewSet.as_view({'get': 'retrieve'}),
        name="category-detail",
    ),
    path(
        "<slug:category_slug>/<slug:sub_category_slug>/",
        SubCategoryViewSet.as_view({'get': 'retrieve'}),
        name="subcategory-detail",
    ),
    path(
        "<slug:category_slug>/<slug:sub_category_slug>/<slug:ad_slug>/",
        AdViewSet.as_view({'get': 'retrieve'}),
        name="ad-detail",
    ),
]
