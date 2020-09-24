
from django.urls import path
from . import views

app_name = "apptwo"
urlpatterns = [
    path('tnku/',views.tnku,name='tnku'),

]
