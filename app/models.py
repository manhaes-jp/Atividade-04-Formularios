from django.db import models

class Titles(models.Model):
  name = models.CharField(max_length=50)
  quantity = models.IntegerField()
  scorer = models.CharField(max_length=20)
  year = models.IntegerField()

class Idols(models.Model):
  POSITIONS = [
    ("G", "Goleiro"),
    ("Z", "Zagueiro"),
    ("L", "Lateral"),
    ("V", "Volante"),
    ("M", "Meia"),
    ("P", "Ponta"),
    ("A", "Atacante"),
  ]
  name = models.CharField(max_length=50)
  games = models.IntegerField()
  position = models.CharField(max_length=1, choices=POSITIONS)
  age = models.CharField(max_length=20)
  