from django.urls import path

from apps.course.api.api import CourseTypeApiView, CourseApiView, CourseReservationApiView

urlpatterns = [
    path('course-type/', CourseTypeApiView.as_view(), name='course-type'),
    path('course/', CourseApiView.as_view(), name='course-type'),
    path('course-reservation/', CourseReservationApiView.as_view(), name='course-reservation'),
]
