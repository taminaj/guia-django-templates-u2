from django.urls import path
from . import views

app_name = "app1"
urlpatterns = [
    path('v1_app1/', views.v1_app1, name='v1_app1'),
]