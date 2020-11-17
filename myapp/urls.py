from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('IEEE', views.ieee),
    path('Springer', views.springer),
    path('ScienceDirect', views.sciencedirect),
    path('ACM', views.acm),
    path('receive_data',views.receive_data)
]