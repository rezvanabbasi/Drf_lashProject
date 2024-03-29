from django.db import models

from apps.users.models import Profile


class LashService(models.Model):
    """
    Created a single lash service like lash extension or ...,
    related to : model:'users.Profile'
    """
    staff = models.ForeignKey(
        Profile,
        related_name='lash_service',
        on_delete=models.CASCADE,
        null=True
    )
    image = models.ImageField(null=True)
    title = models.CharField(max_length=300)
    material = models.TextField(max_length=300)
    price = models.IntegerField(null=True)
    duration = models.TimeField(null=True)
    date = models.DateField(null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ReserveService(models.Model):
    """
    To reserve a single lash service by customer,
    related to :
    model : 'service.LashService',
    model : 'users.Profile'
    """
    service = models.ForeignKey(
        LashService,
        on_delete=models.CASCADE,
        related_name='reserve_service',
        null=True
    )
    customer = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='customer',
        null=True
    )
    fixed_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    comment = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.comment
