from django.urls import path

from tutors import views

app_name = 'tutors'

urlpatterns = [
    path('', views.list, name='list'),
]
