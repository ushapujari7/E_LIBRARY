from django.contrib import admin
from django.urls import path, include
from .views import home  # Import the home view

urlpatterns = [
    path('', home, name='home'),  # ✅ Home page URL
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('users/', include('users.urls')),
    path('registration/', include('users.urls')),  # If using a users app for registration
]
