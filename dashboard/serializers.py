from rest_framework import serializers
from .models import *
class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ['name', 'value']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['width', 'height', 'url']

class OfferSerializer(serializers.ModelSerializer):
    attributes = AttributeSerializer(many=True)
    image = ImageSerializer()

    class Meta:
        model = Offer
        fields = ['id', 'name', 'brand', 'category', 'merchant', 'attributes', 'image']

    def create(self, validated_data):
        attributes_data = validated_data.pop('attributes')
        image_data = validated_data.pop('image')

        image = Image.objects.create(**image_data)
        offer = Offer.objects.create(image=image, **validated_data)

        for attribute_data in attributes_data:
            Attribute.objects.create(offer=offer, **attribute_data)

        return offer