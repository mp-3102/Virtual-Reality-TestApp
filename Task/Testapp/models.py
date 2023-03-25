from django.db import models

# Create your models here.

class Building(models.Model):
    Name = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.Name
    
class Room_Type(models.Model):
    
    Type_Choices = (
        ('S','Single'),
        ('D', 'Double'),
    )
    
    Name = models.CharField(max_length=100, blank=True, null=True)
    Type = models.CharField(max_length=1,  choices=Type_Choices)
    Building = models.ForeignKey(Building, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Name
    
class Room(models.Model):
    Number = models.PositiveSmallIntegerField()
    Room_Type = models.ForeignKey(Room_Type, on_delete=models.CASCADE)
    Price = models.FloatField()
    
  

class BlockedDay(models.Model):
    Day = models.DateField()
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)

