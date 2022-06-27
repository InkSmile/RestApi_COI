from django_filters import rest_framework as filters

from .models import Doctors


class DoctorsFilter(filters.FilterSet):
    ordering = filters.OrderingFilter(fields={
        'date_of_birthday': 'date_of_birthday',
        'work_experience': 'work_experience',
        
    })

    class Meta:
        model = Doctors
        fields = ('direction', 'work_experience')
