from django.db import models
from simple_history.models import HistoricalRecords
from authentication.models import User


class Employer(models.Model):
    user = models.OneToOneField(User, verbose_name='User', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название компании', max_length=255)
    employees_count = models.IntegerField(verbose_name='Число сотрудников')

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работодатель'
        verbose_name_plural = 'Работодатели'


class Finder(models.Model):
    user = models.OneToOneField(User, verbose_name='User', on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    cv = models.FileField(verbose_name='Файл резюме', upload_to='cv', blank=True)
    photo = models.ImageField(verbose_name='Фото', upload_to='img/user_photos', blank=True)

    history = HistoricalRecords()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Соискатель'
        verbose_name_plural = 'Соискатели'


class Vacancy(models.Model):
    company = models.ForeignKey(Employer, verbose_name='Компания', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название вакансии', max_length=255)
    description = models.TextField(verbose_name='Описание вакансии', null=True, blank=True)

    history = HistoricalRecords()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


class Interview(models.Model):
    employer = models.ForeignKey(Employer, verbose_name='Работодатель', on_delete=models.CASCADE)
    finder = models.ForeignKey(Finder, verbose_name='Соискатель', on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, verbose_name='Вакансия', on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='Дата и время проведения')
    STATUS_CHOICES = (('PLANNED', 'Запланировано'), ('PROCESSING', 'В процессе'), ('FINISHED', 'Окончено'))
    status = models.CharField(verbose_name='Статус собеседования', choices=STATUS_CHOICES,max_length=255)

    history = HistoricalRecords()

    def __str__(self):
        return f'{self.employer.name} {self.vacancy.title} - {self.finder.first_name} {self.finder.last_name}'

    class Meta:
        verbose_name = 'Собеседование'
        verbose_name_plural = 'Собеседования'
