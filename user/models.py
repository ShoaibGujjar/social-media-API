from djongo import models
from django.contrib.auth.models import User

# Create your models here.
class CustomUser(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    firstName=models.CharField(max_length=30,null=True)
    lastName=models.CharField(max_length=30,null=True,blank=True)
    jobTitle=models.CharField(max_length=30,null=True,blank=True)
    location=models.CharField(max_length=100,null=True)
    school=models.CharField(max_length=150,null=True,blank=True)
    fbId=models.CharField(primary_key=True,max_length=150)
    birthday=models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.fbId


class UserImage(models.Model):
    fbId = models.ForeignKey(CustomUser,related_name='userimage', on_delete=models.CASCADE)
    image=models.CharField(max_length=300,null=True,blank=True)