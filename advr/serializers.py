from rest_framework import serializers
from advr.models import Category, SubCategory, Ad


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ("title", "description")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("title", "description")


class CategoryListSerializer(CategorySerializer):
    sub_categories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ("title", "description", "sub_categories")


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = (
            "title",
            "description",
            "price",
            "user",
            "created_at",
            "show_count"
        )


class SubCategoryRetrieveSerializers(SubCategorySerializer):
    ads = AdSerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = ("title", "description", "ads")
