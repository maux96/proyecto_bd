from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=200)
    chakra_required = models.IntegerField()
    belong_to_the_village = models.BooleanField()
    element = models.CharField(max_length=50)

    def __str__(self):
        return self.name