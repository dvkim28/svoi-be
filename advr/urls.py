from django.urls import path, include
from rest_framework.routers import DefaultRouter
from advr.views import CategoryViewSet, SubCategoryViewSet, AdViewSet

router = DefaultRouter()

router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"categories/(?P<category_slug>"
                r"[^/]+)/subcategories",
                SubCategoryViewSet,
                basename="subcategory")
router.register(r"categories/(?P<category_slug>[^/]+)"
                r"/subcategories/(?P<sub_category_slug>[^/]+)/ads",
                AdViewSet,
                basename="ad")

urlpatterns = [
    path('', include(router.urls)),
]
