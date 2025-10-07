from django.urls import path
from . import views

def outra_view(request):
    pass

urlpatterns = [
    path('ola/, views_saudacao') ,
    path('outra/, views_outra_view'),
]