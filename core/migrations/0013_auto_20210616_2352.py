# Generated by Django 3.0.7 on 2021-06-17 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20210616_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='candidaturas',
            field=models.IntegerField(default=0, verbose_name='Candidaturas para essa vaga'),
        ),
    ]