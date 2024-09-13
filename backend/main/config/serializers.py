from rest_framework import serializers
from config import models


class CompanySerializer(serializers.ModelSerializer):
    """
    Serializer for the Company model. It ensures all fields are serialized and
    also modifies the representation of the name field to be in title case.
    """
    class Meta:
        model = models.Company
        fields = '__all__'

    def to_representation(self, instance):
        """
        Custom representation method to ensure the company name is returned in title case.
        """
        data = super().to_representation(instance)
        data['name'] = instance.name.title()
        return data


class LocationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Location model. Serializes all fields of the Location model.
    """
    class Meta:
        model = models.Location
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Department model. Serializes all fields of the Department model.
    """
    class Meta:
        model = models.Department
        fields = '__all__'


class DesignationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Designation model. Serializes all fields of the Designation model.
    """
    class Meta:
        model = models.Designation
        fields = '__all__'


class DivisionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Division model. Serializes all fields of the Division model.
    """
    class Meta:
        model = models.Division
        fields = '__all__'


class SubDivisionSerializer(serializers.ModelSerializer):
    """
    Serializer for the SubDivision model. Serializes all fields of the SubDivision model.
    """
    class Meta:
        model = models.SubDivision
        fields = '__all__'


class ShopfloorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Shopfloor model. Serializes all fields of the Shopfloor model.
    """
    class Meta:
        model = models.Shopfloor
        fields = '__all__'


class ShiftSerializer(serializers.ModelSerializer):
    """
    Serializer for the Shift model. Serializes all fields of the Shift model.
    """
    class Meta:
        model = models.Shift
        fields = '__all__'


class AutoShiftSerializer(serializers.ModelSerializer):
    """
    Serializer for the AutoShift model. Serializes all fields of the AutoShift model.
    """
    class Meta:
        model = models.AutoShift
        fields = '__all__'
