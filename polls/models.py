from django.db import models
from django.utils import timezone
import datetime

# Create your models here. Data models


class Question(models.Model): #models.Model is the super class. Inheritance works like this in Python
    question_text = models.CharField(max_length=200) # "question_text" will be used as the DB Column name.
    pub_date = models.DateTimeField('date published') # If a string is provided in the brackets it's used as a human-readable name, otherwise the machine name is used

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # the key is used for relationships. each Choice has a Question as a Key. -> Many to one relation. Perhaps more than one question can have the same key?
    choice_text = models.CharField(max_length=200)                   # The question foreign key thing leads to Django automatically generating a field on each instance called choice_set (classname_set) it's a releated Manager.
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
