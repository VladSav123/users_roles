from django.db import models

class Role(models.Model):
    name=models.CharField(max_length=20)
    
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING)