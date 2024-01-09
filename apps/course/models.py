from django.db import models
from apps.users.models import Profile


class CourseType(models.Model):
    title = models.CharField(max_length=100),
    description = models.TextField(max_length=300)


class Course(models.Model):
    title = models.CharField(max_length=300, default='اکستنشن مژه')
    teacher = models.ForeignKey(
        Profile,
        related_name='course',
        on_delete=models.CASCADE,
        null=True
    )
    course_capacity = models.IntegerField(default=1, null=True)
    course_sessions = models.IntegerField(default=5)  # Number of course sessions
    course_start_date = models.DateTimeField(auto_now_add=True)  # Time and date of course holding
    course_session_duration = models.IntegerField(null=True)
    is_available = models.BooleanField(default=False)
    comment = models.TextField(max_length=300, null=True)

    def __str__(self):
        return self.title


class CourseReservation(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='course_reservation',
        null=True
    )
    student = models.ForeignKey(
        Profile,
        related_name='student',
        on_delete=models.CASCADE,
        null=True
    )
    reserve_date = models.DateTimeField(auto_now_add=True)

