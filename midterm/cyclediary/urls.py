from django.urls import path, re_path
from cyclediary import views

app_name = 'cyclediary'
urlpatterns = [
    path('', views.CyclediaryLV.as_view(), name='index'),
    path('cyclediary/', views.CyclediaryLV.as_view(), name='cyclediary_list'),
    re_path(r'^cyclediary/(?P<slug>[-\w]+)/$', views.CyclediaryDV.as_view(), name='cyclediary_detail'),
    path('archive/', views.CyclediaryAV.as_view(), name='cyclediary_archive'),
    path('archive/<int:year>/', views.CyclediaryYAV.as_view(), name='cyclediary_year_archive'),
    path('archive/<int:year>/<str:month>/', views.CyclediaryMAV.as_view(), name='cyclediary_month_archive'),
    path('archive/<int:year>/<str:month>/<int:day>/', views.CyclediaryDAV.as_view(), name='cyclediary_day_archive'),
    path('archive/today/', views.CyclediaryTAV.as_view(), name='cyclediary_today_archive'),
    path('search/', views.SearchFormView.as_view(), name='search'),
]