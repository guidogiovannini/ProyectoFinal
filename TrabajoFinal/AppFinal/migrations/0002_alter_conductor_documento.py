# Generated by Django 4.0.4 on 2022-05-08 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conductor',
            name='Documento',
            field=models.IntegerField(),
        ),
    ]