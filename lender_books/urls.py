from .views import book_list_view
from django.urls import path


urlpatterns = [
    path('', book_list_view, name='book_list'),
]
