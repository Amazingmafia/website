from django.db import models

# Create your models here.
class links(models.Model):
    def __str__(self):
        return self.string_name if self.string_name else "No Name"
    address=models.CharField(max_length=500,null=True,blank=True)
    string_name=models.CharField(max_length=500,null=True,blank=True)
