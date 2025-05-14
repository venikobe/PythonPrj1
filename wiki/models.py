from django.db import models
from django.urls import reverse

class Page(models.Model):

    PageTitle = models.CharField(verbose_name = 'Заголовок', default="Заголовок", max_length=350)
    PageUrl = models.CharField(verbose_name = 'Ссылка', default="default", max_length=350)
    PagePriority = models.IntegerField(verbose_name = 'Приоритет', default=1)
    PageContent = models.TextField(verbose_name = 'Основное содержание страницы', default ='<p>Привет</p>')
    currenttime = models.DateTimeField(verbose_name = "Дата изменения", auto_now=True)

    class Meta:
        verbose_name = 'Контент текущей страницы'
        verbose_name_plural = 'Уникальный контент страниц'
        ordering = ('-PagePriority',)

    def __str__(self):
        return f"id: {self.id}.  {self.PageTitle}"
