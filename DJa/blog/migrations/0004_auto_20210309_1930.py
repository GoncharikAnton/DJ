# Generated by Django 3.1.7 on 2021-03-09 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210304_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tag', to='blog.Tag', verbose_name='Тег'),
        ),
    ]