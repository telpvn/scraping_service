from django.db import models

from scraping.utils import from_cyrillic_to_eng


class City(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Название населенного пункта',
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Название населенного пункта'
        verbose_name_plural = 'Название населенных пунктов'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Язык программирования',
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Vacancy(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=250, verbose_name='')
    company = models.CharField(max_length=250, verbose_name='')
    description = models.TextField(verbose_name='')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='')
    Language = models.ForeignKey('Language', on_delete=models.CASCADE,
                                 verbose_name='')








