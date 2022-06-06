from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Dog(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    verified_dog = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Puppy(models.Model):
    name = models.CharField(max_length=100)
    dog = models.ForeignKey(
        Dog, on_delete=models.CASCADE, related_name="puppies")
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Litter(models.Model):
    title = models.CharField(max_length=100)
    puppies = models.ManyToManyField(Puppy)

    def __str__(self):
        return self.title
