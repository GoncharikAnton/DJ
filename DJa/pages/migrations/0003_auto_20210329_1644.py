# Generated by Django 3.1.7 on 2021-03-29 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20210329_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='edit_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата редактирования'),
        ),
    ]
