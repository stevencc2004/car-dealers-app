from rest_framework import serializers

class DealerSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=200)
    city = serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=300)
    zip_code = serializers.CharField(max_length=20)
    phone = serializers.CharField(max_length=20)
    description = serializers.CharField(required=False, allow_blank=True)
    image_url = serializers.URLField(required=False, allow_blank=True)

class ReviewSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    dealer_id = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=200)
    review = serializers.CharField()
    sentiment = serializers.CharField(read_only=True)
    user = serializers.CharField(max_length=200)

class CarBrandSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=200)

class CarModelSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    brand = serializers.CharField(max_length=200)
    model = serializers.CharField(max_length=200)
    year = serializers.IntegerField()
    price = serializers.FloatField()