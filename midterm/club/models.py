from django.db import models
from django.urls import reverse


class Club(models.Model):
    name = models.CharField('CLUB NAME', max_length=100, blank=False)
    city = models.CharField('CLUB CITY', max_length=50, blank=True)
    tel = models.CharField('MOBILE', max_length=50, blank=True)
    content = models.TextField('CONTENT', blank=True)
    location = models.CharField('MEETING PLACE', max_length=50, blank=False)
    riding_dt = models.DateTimeField('MEETING DATE', auto_now=False)
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)

    class Meta:
        ordering = ('-riding_dt',)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('club:detail', args=(self.id,))
