from django.urls import path
from .views import home, about
# search_create






urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
]