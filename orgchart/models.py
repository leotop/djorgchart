from django.db import models

# Create your models here.


class OrgChartModel(models.Model):
    Title = models.CharField(max_length=300, verbose_name='Название ПС')
    Content = models.TextField(verbose_name='Cодержание')

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'

    def __str__(self):
        result = self.Title
        return result