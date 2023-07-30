from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# here table name is room and we use Model from ligrary models

class Topic(models.Model):
    name= models.CharField(max_length=150)
    def __str__(self):
        return self.name

class Room(models.Model):
    host=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic= models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants= models.ManyToManyField(User, related_name='participants', blank=True) #basically a user can have many rooms and a room cal have many user
    updated = models.DateTimeField(auto_now=True) #changes everytime
    created = models.DateTimeField(auto_now_add=True) #chnages once when we open first time
#blank=True basically allows you to submit without actually filling that thing
    class Meta:
        ordering = ['-updated', '-created'] #gives prefrence,  with -(acsending), without -(descending)

    def __str__(self):
        return self.name

class Message(models.Model):
    user=  models.ForeignKey(User, on_delete=models.CASCADE) #user is built in by django we access it importing the above library or wtvr
    room= models.ForeignKey(Room, on_delete=models.CASCADE) #if a room is delted then the mesg of respective group are also deleted
    body= models.TextField()
    updated = models.DateTimeField(auto_now=True) #changes everytime
    created = models.DateTimeField(auto_now_add=True) #chnages once when we open first time
    
    class Meta:
        ordering = ['-updated', '-created']
        
    def __str__ (self):
        return self.body[0:50]