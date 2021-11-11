from django.db import models

class New(models.Model):
    time = models.CharField('Время', max_length=50)
    predmet = models.CharField('Предмет', max_length=50)
    title = models.CharField('Преподаватель', max_length=50)
    kab = models.CharField('Кабинет', max_length=50)

    def __str__(self):
        return f'Время: {self.time}'

    class Meta:
        verbose_name = 'расписание'
        verbose_name_plural = 'расписание'

class TimeTable(models.Model):
    day = models.CharField('День', max_length=50)
    time = models.CharField('Время', max_length=50)
    predmet = models.CharField('Предмет', max_length=50)
    title = models.CharField('Преподаватель', max_length=50)
    kab = models.CharField('Кабинет', max_length=50)

    def __str__(self):
        return '%s' % (self.day)

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'