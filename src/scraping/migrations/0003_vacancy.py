# Generated by Django 3.0.14 on 2022-09-22 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0002_auto_20220920_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок вакансии')),
                ('company', models.CharField(max_length=250, verbose_name='Компания')),
                ('description', models.TextField(verbose_name='Описание вакансии')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('Language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.Language', verbose_name='Язык программирования')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.City', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Вакансии',
                'verbose_name_plural': 'Вакансии',
            },
        ),
    ]
