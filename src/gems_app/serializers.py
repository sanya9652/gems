from rest_framework import serializers


class RichSerializer(serializers.Serializer):
    username = serializers.CharField(source='customer')
    spent_money = serializers.FloatField()
    gems = serializers.ListField(child=serializers.CharField())