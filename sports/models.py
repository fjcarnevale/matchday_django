from django.db import models

# Create your models here.

class League(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Team(models.Model):
  name = models.CharField(max_length=20)
  league = models.ForeignKey(League)

  def __str__(self): 
    return self.name

class Match(models.Model):
  date = models.DateTimeField()
  home = models.ForeignKey(Team, related_name='home', default=None)
  away = models.ForeignKey(Team, related_name='away', default=None)
