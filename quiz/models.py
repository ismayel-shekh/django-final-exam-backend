from django.db import models
from participator.models import participator
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=40)
    def __str__(self):
        return self.name
    
class Quiz(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    catagory = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.TextField()
    point = models.IntegerField()
    def __str__(self):
        return self.question

class Choice(models.Model):
    question_choice = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_currect = models.BooleanField(default=False)
    def __str__(self):
        return self.question_choice.question
    

STAR_CHOICES=[
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐⭐⭐'),

]
class Review(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    reviewer_Name = models.CharField(max_length=200)
    rating = models.CharField(choices =STAR_CHOICES, max_length =15)
    def __str__(self):
        return self.reviewer_Name