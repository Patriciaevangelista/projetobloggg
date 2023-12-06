# Generated by Django 5.0 on 2023-12-05 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='resumo',
        ),
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(null=True),
        ),
    ]