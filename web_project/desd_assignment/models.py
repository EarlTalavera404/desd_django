from django.db import models
from django.utils import timezone

class ClubRep(models.Model):
    repNumber = models.PositiveIntegerField()
    firstName = models.CharField(max_length=100)#add a default value cause of id generation
    lastName = models.CharField(max_length=500)
    password = models.CharField(max_length=100)
    dob = models.CharField(max_length=10)




class Films(models.Model):
    title = models.CharField(max_length=100)
    ageRating = models.PositiveIntegerField()
    duration = models.CharField(max_length=100)
    filmImage = models.ImageField(null=True, blank=True,upload_to='images/')
    filmDescription = models.CharField(max_length=500,default ="Description")


