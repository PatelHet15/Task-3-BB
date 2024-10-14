# task3/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('q.urls')),  
    path('', RedirectView.as_view(url='/products/', permanent=False)),  
]
