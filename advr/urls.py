from django.urls import path, include
from rest_framework import routers

from advr import views

router = routers.DefaultRouter()
router.register("categories", views.AdMainViewView)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "store_service"
