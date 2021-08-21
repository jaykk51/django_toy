from django.urls import path, re_path
from map import views


app_name = 'map'
urlpatterns = [
    path('', views.mapLV.as_view(), name='index'),
    path('<int:pk>/', views.mapDV.as_view(), name='detail'),
    path('search/', views.SearchFormView.as_view(), name='search'),
]