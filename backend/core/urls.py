from django.contrib import admin
from django.urls import path
from backend.app import menyu_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menyu_view, name='home'), # Asosiy sahifa
]
