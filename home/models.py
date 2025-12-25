from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='person_images/')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "People"
