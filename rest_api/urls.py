from django.urls import path, include

from .views import DirectionApiList, DoctorApiList

urlpatterns = [
    path('directions/', DirectionApiList.as_view()),
    path('doctors/', DoctorApiList.as_view())
]