from django.urls import path, re_path
from club import views


app_name = 'club'
urlpatterns = [
    path('', views.clubLV.as_view(), name='index'),
    path('<int:pk>/', views.clubDV.as_view(), name='detail'),
    path('search/', views.SearchFormView.as_view(), name='search'),

]