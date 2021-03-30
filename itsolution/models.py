from django.db import models


class messageFromSpace(models.Model):
    msg_text = models.TextField('Текст сообщения')
    msg_date = models.DateTimeField('Дата публикации')
    msg_read = models.BooleanField('Флаг прочитанного сообщения', default=False)

    def __str__(self):
        return self.msg_text

    def hasread(self):
        return self.msg_read

    def mark_read(self):
        self.msg_date = True
        self.save()
        return

    class Meta:
        verbose_name = 'Сообщение из космоса'
        verbose_name_plural = 'Сообщения из космоса'
