from django.urls import path
from . import views

app_name = "app3"
urlpatterns = [
    path('v1_app3/', views.v1_app3, name='v1_app3'),
]