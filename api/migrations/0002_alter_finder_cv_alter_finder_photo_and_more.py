# Generated by Django 4.0.4 on 2022-05-29 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finder',
            name='cv',
            field=models.FileField(null=True, upload_to='cv', verbose_name='Файл резюме'),
        ),
        migrations.AlterField(
            model_name='finder',
            name='photo',
            field=models.ImageField(null=True, upload_to='img/user_photos', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='status',
            field=models.CharField(choices=[('PLANNED', 'Запланировано'), ('PROCESSING', 'В процессе'), ('FINISHED', 'Окончено')], max_length=255, verbose_name='Статус собеседования'),
        ),
    ]
