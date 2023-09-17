from rest_framework import serializers
from core import models


class UnitShort(serializers.ModelSerializer):
    class Meta:
        model = models.Unit
        fields = ('id', 'name')


class Coder(serializers.ModelSerializer):
    score = serializers.SerializerMethodField()
    units = UnitShort(many=True)

    class Meta:
        model = models.Coder
        fields = '__all__'

    def get_score(self, obj: models.Coder) -> int:
        return obj.get_score()
