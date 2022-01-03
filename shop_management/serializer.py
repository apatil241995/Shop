from rest_framework import serializers
from shop_management import models


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Items
        fields = '__all__'



class ShopOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Owner
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shop
        fields = '__all__'


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sales
        fields = '__all__'
