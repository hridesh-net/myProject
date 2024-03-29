from django.db import models

# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    author = models.CharField(max_length=50)
    summary = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name