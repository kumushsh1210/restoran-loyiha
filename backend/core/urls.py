from django.contrib import admin
from django.urls import path
from app.views import menyu_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menyu_view, name='home'), # Asosiy sahifa
]
