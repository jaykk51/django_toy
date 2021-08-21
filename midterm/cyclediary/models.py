from django.db import models
from django.urls import reverse


# Create your models here.

class Cyclediary(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True,
                            help_text='one word for title alias.')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True,
                                   help_text='simple description text')
    #부제목, 디스크립션
    diary_dt = models.DateField('DIARY DATE', auto_now=False)
    #지난주 기록을 빠뜨렸을 때,그 날의 기록임을 기억하기 위해 작성시간, 수정시간과는 별개로 날짜를 지정해줌
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)

    class Meta:
        verbose_name = 'diary'
        verbose_name_plural = 'diaries'
        ordering = ('-diary_dt',)
        #일기 날짜 내림차순

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cyclediary:cyclediary_detail', args=(self.slug,))

    def get_previous(self):
        return self.get_previous_by_diary_dt()

    def get_next(self):
        return self.get_next_by_diary_dt()



