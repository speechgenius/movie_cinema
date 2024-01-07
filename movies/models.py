from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()

    def __str__(self):
        return f'title: {self.title} year: {self.year}'
    
class Member(models.Model):
    name =models.CharField(max_length=20)
    membership_number=models.CharField(max_length=10)
    
    