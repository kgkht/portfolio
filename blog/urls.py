from django.urls import path
from .views import allblogs

app_name = 'blog'

urlpatterns = [
    path('', allblogs, name='allblogs'),
]
