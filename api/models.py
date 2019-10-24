from django.db import models
from django.http import HttpResponse
from django.core.validators import validate_email, validate_ipv4_address, MinLengthValidator

class LambdaF(models.Model):
    lst = models.CharField(max_length=50)

class api_lambdaf(models.Model):
    lst = models.CharField(max_length=50)

    @property
    def ordered_list(self, lst):
        return HttpResponse({'solution': lst.data})
        # data=lst.data
    def __str__(self):
       return {'solution': self.lst}
