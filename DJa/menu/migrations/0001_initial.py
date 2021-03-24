# Generated by Django 3.1.7 on 2021-03-22 15:37

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название')),
                ('is_auth', models.BooleanField(default=False, verbose_name='Для зарегистрированных')),
                ('active', models.BooleanField(default=True, verbose_name='Активно вкл/выкл')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
        migrations.CreateModel(
            name='MenuPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название на латинице')),
                ('title', models.CharField(max_length=300, verbose_name='Название на русском')),
                ('status', models.BooleanField(default=True, verbose_name='Вкл/выкл')),
                ('is_auth', models.BooleanField(default=False, verbose_name='Для зарегистрированных')),
                ('anchor', models.CharField(max_length=300, verbose_name='Якорь')),
                ('url', models.URLField(max_length=500)),
                ('active', models.BooleanField(default=True, verbose_name='Активно вкл/выкл')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='menu.menu', verbose_name='Меню')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menu.menupoint', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Пункт меню',
                'verbose_name_plural': 'Пункты меню',
            },
        ),
    ]