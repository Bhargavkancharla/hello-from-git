from django.urls import path
from .import views

urlpatterns = [
    path('api/',views.booklist),
    path('details/<int:pk>/',views.bookdetails),
]
