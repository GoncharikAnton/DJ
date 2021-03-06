# Generated by Django 3.1.7 on 2021-03-31 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(help_text='Введите свои ФИО', max_length=500, verbose_name='ФИО')),
                ('text', models.TextField(max_length=2500, verbose_name='Текст сообщения')),
                ('email', models.EmailField(help_text='Введите свою электронную почту', max_length=500, verbose_name='email')),
                ('created_date', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Форма обратной связи',
                'verbose_name_plural': 'Формы обратной связи',
            },
        ),
    ]
