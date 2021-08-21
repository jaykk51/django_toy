from django.contrib import admin
from django.urls import path, include
from midterm.views import HomeView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('cyclenumber/', include('cyclenumber.urls')),
    path('cyclediary/', include('cyclediary.urls')),
    path('club/', include('club.urls')),
    path('map/', include('map.urls')),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
