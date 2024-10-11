from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

        # fields = "__all__"  # 모든 항목 표시
        fields = (
            "name",
            "kind",
        )
        # exclude = ("created_at",)  # 제외 항목 표시
