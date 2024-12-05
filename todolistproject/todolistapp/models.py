from django.db import models
from django.utils import timezone

# Create your models here.
class task(models.Model):
    name=models.TextField()
    datetime=models.DateTimeField(default=timezone.now)
    complete=models.BooleanField(default=False,blank=True,null=True)
    
    def __str__(self):
        return self.name