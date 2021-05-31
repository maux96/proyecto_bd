from django.db import models
from django.urls import reverse
from django.apps import apps

# Create your models here.
class Invocation(models.Model):
    name = models.CharField(max_length=200)
    invocation_type = models.CharField(max_length=200)

    def contract_by(self):
        return apps.get_model('ninjas','Ninja').objects.filter(invocations=self.pk) 

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('invocations:invocation_detail', kwargs={'pk': self.pk})