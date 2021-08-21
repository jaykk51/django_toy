from django.db import models
from django.urls import reverse


class Cyclenumber(models.Model):
    name = models.CharField('NAME', max_length=100, blank=False)
    tel = models.CharField('MOBILE', max_length=50, blank=False)
    brand = models.CharField('BRAND', max_length=50, blank=True)
    modelname = models.CharField('MODEL NAME', max_length=50, blank=True)
    number = models.CharField('CYCLE NUMBER', max_length=50, blank=False, unique=True)
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)

#   class Meta:
#       ordering = ('number', 'name')

    def __str__(self):
        return self.number


    def get_absolute_url(self):
        return reverse('cyclenumber:detail', args=(self.id,))