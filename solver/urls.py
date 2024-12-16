from django.urls import path
from . import views

urlpatterns = [
    path('', views.solve_puzzle, name='solve_puzzle'),
]
