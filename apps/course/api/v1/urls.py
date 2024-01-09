from django.urls import path

from apps.course.api.v1.api import CourseTypeApiView, CourseApiView, CourseReservationApiView

urlpatterns = [
    path('course-type/', CourseTypeApiView.as_view(), name='course-type'),
    path('course/', CourseApiView.as_view(), name='course'),
    path('course-reservation/', CourseReservationApiView.as_view(), name='course-reservation'),
]
