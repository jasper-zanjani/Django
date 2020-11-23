from django.db import models

# Create your models here.

class StarshipClass(models.Model):
  name= models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Starship(models.Model):
  Name = models.CharField(max_length=50)
  Registry = models.CharField(max_length=50, )
  StarshipClass = models.ForeignKey(StarshipClass, on_delete=models.CASCADE, )
  Crew = models.IntegerField()
  Image = models.ImageField(null=True, blank=True)

  def __str__(self):
    return f'{self.Name} ({self.Registry})'