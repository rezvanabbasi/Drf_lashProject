from django.urls import path, include


urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('services/', include('apps.services.urls')),
    path('course/', include('apps.course.urls')),
    path('home/', include('apps.home.urls')),
]