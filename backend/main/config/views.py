from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from django.core.cache import cache
from datetime import datetime, timedelta
import pytz
from config import models
from config import serializers


class DefaultPagination(PageNumberPagination):
    """
    Pagination class to set default pagination for list views.
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


# Company Views

class CompanyListCreate(generics.ListCreateAPIView):
    """
    List and create Company instances.
    """
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    pagination_class = DefaultPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['name', 'code', 'created_at', 'updated_at']
    search_fields = ['name', 'code', 'created_at', 'updated_at']
    ordering_fields = '__all__'


class CompanyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a single Company instance.
    """
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    lookup_url_kwarg = "id"


# Location Views

class LocationListCreate(generics.ListCreateAPIView):
    """
    List and create Location instances.
    """
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer
    pagination_class = DefaultPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['name', 'code', 'created_at', 'updated_at']
    search_fields = ['name', 'code', 'created_at', 'updated_at']
    ordering_fields = '__all__'


class LocationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a single Location instance.
    """
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer
    lookup_url_kwarg = "id"


# Department Views

class DepartmentListCreate(generics.ListCreateAPIView):
    """
    List and create Department instances.
    """
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    pagination_class = DefaultPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['name', 'code', 'created_at', 'updated_at']
    search_fields = ['name', 'code', 'created_at', 'updated_at']
    ordering_fields = '__all__'


class DepartmentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a single Department instance.
    """
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    lookup_url_kwarg = "id"


# Designation Views

class DesignationListCreate(generics.ListCreateAPIView):
    """
    List and create Designation instances.
    """
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer
    pagination_class = DefaultPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['name', 'code', 'created_at', 'updated_at']
    search_fields = ['name', 'code', 'created_at', 'updated_at']
    ordering_fields = '__all__'


class DesignationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a single Designation instance.
    """
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer
    lookup_url_kwarg = "id"


# Division Views

class DivisionListCreate(generics.ListCreateAPIView):
    """
    List and create Division instances.
    """
    queryset = models.Division.objects.all()
    serializer_class = serializers.DivisionSerializer
    pagination_class = DefaultPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['name', 'code', 'created_at', 'updated_at']
    search_fields = ['name', 'code', 'created_at', 'updated_at']
    ordering_fields = '__all__'


class DivisionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a single Division instance.
    """
    queryset = models.Division.objects.all()
    serializer_class = serializers.DivisionSerializer
    lookup_url_kwarg = "id"


# SubDivision Views

class SubDivisionListCreate(generics.ListCreateAPIView):
    """
    List and create SubDivision instances.
    """
    queryset = models.SubDivision.objects.all()
    serializer_class = serializers.SubDivisionSerializer
    pagination_class = DefaultPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['name', 'code', 'created_at', 'updated_at']
    search_fields = ['name', 'code', 'created_at', 'updated_at']
    ordering_fields = '__all__'


class SubDivisionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a single SubDivision instance.
    """
    queryset = models.SubDivision.objects.all()
    serializer_class = serializers.SubDivisionSerializer
    lookup_url_kwarg = "id"


# Shopfloor Views

class ShopfloorListCreate(generics.ListCreateAPIView):
    """
    List and create Shopfloor instances.
    """
    queryset = models.Shopfloor.objects.all()
    serializer_class = serializers.ShopfloorSerializer
    pagination_class = DefaultPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['name', 'code', 'created_at', 'updated_at']
    search_fields = ['name', 'code', 'created_at', 'updated_at']
    ordering_fields = '__all__'


class ShopfloorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a single Shopfloor instance.
    """
    queryset = models.Shopfloor.objects.all()
    serializer_class = serializers.ShopfloorSerializer
    lookup_url_kwarg = "id"


# Shift Views

class ShiftListCreate(generics.ListCreateAPIView):
    """
    List and create Shift instances.
    """
    queryset = models.Shift.objects.all()
    serializer_class = serializers.ShiftSerializer
    pagination_class = DefaultPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['name', 'created_at', 'updated_at']
    search_fields = ['name', 'created_at', 'updated_at']
    ordering_fields = '__all__'


class ShiftRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a single Shift instance.
    """
    queryset = models.Shift.objects.all()
    serializer_class = serializers.ShiftSerializer
    lookup_url_kwarg = "id"


# AutoShift Views

class AutoShiftListCreate(generics.ListCreateAPIView):
    """
    List and create AutoShift instances.
    """
    queryset = models.AutoShift.objects.all()
    serializer_class = serializers.AutoShiftSerializer
    pagination_class = DefaultPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'


class AutoShiftRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a single AutoShift instance.
    """
    queryset = models.AutoShift.objects.all()
    serializer_class = serializers.AutoShiftSerializer
    lookup_url_kwarg = "id"


class LastUpdatedAtAPIView(APIView):
    """
    API view to retrieve the last updated timestamp for various models and calculate
    the time difference between the current time and the last update.
    """

    def get(self, request):
        data = {}

        # Define a list of models to iterate over
        model_classes = [
            models.Company,
            models.Location,
            models.Department,
            models.Designation,
            models.Division,
            models.SubDivision,
            models.Shopfloor,
            models.Shift,
        ]

        # Iterate over each model to get the latest updated_at timestamp
        for model_class in model_classes:
            try:
                latest_object = model_class.objects.latest('updated_at')
                latest_update_time = latest_object.updated_at
                data[model_class.__name__] = latest_update_time
            except model_class.DoesNotExist:
                data[model_class.__name__] = None

        # Convert the current time to Indian Standard Time (IST)
        ist_timezone = pytz.timezone('Asia/Kolkata')
        current_time = datetime.now(ist_timezone)

       # Calculate the 'last updated at' time based on the current time and the latest update time from the model
        for key, value in data.items():
            if value:
                # Convert the value to Indian Standard Time (IST)
                value_ist = value.astimezone(ist_timezone)
                time_difference = current_time - value_ist

                # Calculate years, months, days, hours, and minutes in the time difference
                years = time_difference.days // 365
                months = (time_difference.days % 365) // 30
                weeks = (time_difference.days % 365) // 7
                days = time_difference.days % 7
                hours = time_difference.seconds // 3600
                minutes = (time_difference.seconds % 3600) // 60

                # Round off the time difference to the nearest minute, hour, day, month, or year
                if years > 1:
                    last_updated_at = f"Updated {years} years ago"
                elif 0 < years >= 1:
                    last_updated_at = f"Updated {years} year ago"
                elif months > 1:
                    last_updated_at = f"Updated {months} months ago"
                elif 0 < months >= 1:
                    last_updated_at = f"Updated {months} month ago"
                elif weeks > 0:
                    last_updated_at = f"Updated {weeks} weeks ago"
                elif 0 < weeks >= 1:
                    last_updated_at = f"Updated {weeks} week ago"
                elif days > 1:
                    last_updated_at = f"Updated {days} days ago"      
                elif 0 < days >= 1:
                    last_updated_at = f"Updated {days} day ago"                
                elif hours > 1:
                    last_updated_at = f"Updated {hours} hours ago"
                elif 0 < hours >= 1:
                    last_updated_at = f"Updated {hours} hour ago"
                elif minutes > 1:
                    last_updated_at = f"Updated {minutes} minutes ago"
                elif 0 < minutes >= 1:
                    last_updated_at = f"Updated {minutes} minute ago"
                else:
                    last_updated_at = "Updated just now"

                data[key] = last_updated_at
            else:
                data[key] = 'Never Updated'

        return Response(data)