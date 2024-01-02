from django.db import models
from apps.users.models import Profile


class PrivateCourse(models.Model):
    title = models.CharField(max_length=300, default='اکستنشن مژه')
    teacher = models.ForeignKey(
        Profile,
        related_name='course',
        on_delete=models.CASCADE,
        null=True
    )
    student = models.ForeignKey(
        Profile,
        related_name='student',
        on_delete=models.CASCADE,
        null=True
    )

    course_sessions = models.IntegerField(default=5)  # Number of course sessions
    course_start_date = models.DateTimeField(auto_now_add=True)  # Time and date of course holding
    course_duration = models.TimeField(null=True)
    finished = models.BooleanField(default=False)
    comment = models.TextField(max_length=300, null=True)

