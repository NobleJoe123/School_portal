from django.urls import path
from .views import home
# search_create






urlpatterns = [
    path('', home, name='home'),
]