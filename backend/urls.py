from django.contrib import admin
from django.urls import path, include
from contact.views import home  # 👈 import the home view directly

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='root'),              # 👈 handles the root /
    path('contact/', include('contact.urls')),
]
