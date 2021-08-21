from django.urls import path, re_path
from cyclenumber import views


app_name = 'cyclenumber'
urlpatterns = [
    path('', views.cyclenumberLV.as_view(), name='index'),
    path('<int:pk>/', views.cyclenumberDV.as_view(), name='detail'),
    path('search/', views.SearchFormView.as_view(), name='search'),
]