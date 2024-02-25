from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class participator(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='participator/image/')
    mobile_no = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(default=0)
    complete = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"