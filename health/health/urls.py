from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('api.urls')),  # Đảm bảo rằng đường dẫn này đã được thêm
]