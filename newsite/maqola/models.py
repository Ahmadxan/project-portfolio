from django.db import models
    
    
class GetInTouch(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=13, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name