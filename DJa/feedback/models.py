from django.db import models


class FeedBack(models.Model):
    """Feedback model"""

    user_name = models.CharField('ФИО', max_length=500, help_text='Введите свои ФИО')
    text = models.TextField('Текст сообщения', max_length=2500)
    email = models.EmailField('email', max_length=500, help_text='Введите свою электронную почту')

    # def __str__(self):
    #     return self.email

    class Meta:
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Формы обратной связи'
