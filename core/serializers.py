from rest_framework import serializers
from core import models


class Coder(serializers.ModelSerializer):
    score = serializers.SerializerMethodField()

    class Meta:
        model = models.Coder
        fields = '__all__'

    def get_score(self, obj: models.Coder) -> int:
        return obj.get_score()
