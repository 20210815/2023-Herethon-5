from django.urls import path
from goals import views

app_name="goals"

urlpatterns = [
    path('mainpage', views.mainpage, name='mainpage'),
    
]
