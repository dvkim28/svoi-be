from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from advr.models import Category
from advr.serializers import CategorySerializer


class AdMainViewView(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
