from rest_framework import serializers
from rent.models import Rent, Product, RentProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id', 'price', 'name')


class RentProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = RentProduct
        fields = ('product', 'rent_price')
        read_only_fields = ('id', 'rent_price')


class RentSerializer(serializers.ModelSerializer):

    rent_products = RentProductSerializer(
        many=True, required=True)

    class Meta:
        model = Rent
        fields = ('start_date', 'end_date', 'rent_products')
        read_only_fields = ('id', 'rent_duration', 'total_price')

    def create(self, validated_data):
        rent_products = validated_data.pop('rent_products', [])
        rent = Rent.objects.create(**validated_data)

        for rent_product in rent_products:
            RentProduct.objects.create(rent=rent, **rent_product)

        return rent

    def validate_rent_products(self, rent_products_data):
        for rent_product_data in rent_products_data:
            start_date = rent_product_data.get('start_date')
            end_date = rent_product_data.get('end_date')

            if start_date and end_date:
                conflicting_rents = Rent.objects.filter(
                    start_date__lte=end_date,
                    end_date__gte=start_date
                )
                for conflicting_rent in conflicting_rents:
                    conflicting_rent_products = conflicting_rent.rent_products_set.all()
                # Can't handle
                if conflicting_rent_products.exists():
                    raise serializers.ValidationError(
                        "RentProduct with conflicting dates already exists."
                    )
        return rent_products_data
