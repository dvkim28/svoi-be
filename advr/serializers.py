from rest_framework import serializers

from advr.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("title", "slug", "description")
