from django.urls import path
from .views import allblogs, blogpostdetail

app_name = 'blog'

urlpatterns = [
    path('', allblogs, name='allblogs'),
    path('<int:blog_id>/', blogpostdetail, name='blogpost'),
]
