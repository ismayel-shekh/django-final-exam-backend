from django.db import models
from participator.models import participator
# Create your models here.
class quiz_history(models.Model):
    participator = models.OneToOneField(participator, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100) 
    score = models.IntegerField()
    complite_quiz = models.IntegerField()
    def __str__(self):
        return f"{self.participator.user.first_name} {self.participator.user.last_name}"
