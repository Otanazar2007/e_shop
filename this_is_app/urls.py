from django.urls import path
from this_is_app import views


urlpatterns = [
    path('', views.home_page, name='home')
]