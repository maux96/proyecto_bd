from django.db import models

# Create your models here.
class Invocation(models.Model):
    name = models.CharField(max_length=200)
    invocation_type = models.CharField(max_length=200)

    def __str__(self):
        return self.name