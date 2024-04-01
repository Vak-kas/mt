from django.db import models

# Create your models here.

class Card(models.Model):
    num = models.IntegerField(help_text="고유번호")
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)