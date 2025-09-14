import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def total_votes(self):
        votes = 0
        choices = self.choice_set.all()
        # Faça um laço para somar todos os votos.
        for choice in choices:
            votes += choice.votes            
        return votes

    def has_votes(self):
        # Utilize uma condição para retornar se essa Questão tem ou não votos.
        return self.total_votes() > 0


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
