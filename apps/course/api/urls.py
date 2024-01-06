from django.urls import path

from apps.course.api.api import CourseTypeApiView, CourseViewSet

urlpatterns = [
    path('course-type/', CourseTypeApiView.as_view(), name='course-type'),
    path('course/', CourseViewSet.as_view({'post': 'create', 'get': 'list'}), name='course-type'),
]
