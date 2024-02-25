from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path("<str:number>",views.anyNumber,name="anyNumber"),
    path("taxrate",views.taxRate,name="taxRate")
]
