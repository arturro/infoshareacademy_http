from django.urls import path

from . import views

app_name = 'frontend'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    path('vue/', views.VueView.as_view(), name='vue'),
]
