from django.db import models


class Workers(models.Model):
    name = models.CharField(verbose_name='Фио', max_length=100)
    phone = models.CharField(verbose_name='Телефон', max_length=20)
    email = models.EmailField(verbose_name='Почтовый адрес', max_length=100)
    created_at = models.DateTimeField(verbose_name='Дата регистрации', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Дата обновления', auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    def get_pk(self):
        return self.pk

    def get_absolute_url(self):
        return f'/workers/{self.id}'

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


class Professions(models.Model):
    profession = models.CharField('Профессия', max_length=50)

    def __str__(self):
        return self.profession

    def get_pk(self):
        return self.pk

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'


class WorkerProfession(models.Model):
    worker = models.ForeignKey('Workers', on_delete=models.PROTECT, null=True)
    prof = models.ForeignKey('Professions', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.worker.__str__() + self.prof.__str__()

    class Meta:
        verbose_name = 'Связь работник-профессия'
        verbose_name_plural = 'Связи работники-профессии'


