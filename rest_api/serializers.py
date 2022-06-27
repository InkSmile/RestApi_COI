from rest_framework import serializers

from .models import Directions, Doctors


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directions
        fields = ('id', 'name', 'slug', 'sort_number')


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = (
            'id', 'name', 'direction', 'sort_number',
             'description', 'date_of_birthday',
              'work_experience', 'slug'
            )