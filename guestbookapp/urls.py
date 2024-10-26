from django.urls import path
from .views import index,guest_book

urlpatterns = [
    path('', index, name='index'),
    path('guest-book/', guest_book, name='guest_book'),
]
