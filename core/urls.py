from django.urls import path
from .views import HomePageView, SamplePageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),              #Método as_view() para devolverlo como una vista
    path('sample/', SamplePageView.as_view(), name="sample"),
]