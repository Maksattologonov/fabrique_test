from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from polls.managers import CustomUserManager


class BaseUser(AbstractBaseUser):
    username = models.CharField(max_length=50, verbose_name=_('Пользователь'), unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    class Meta:
        db_table = 'usr'
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def __str__(self):
        return self.username


class Poll(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Название'))
    date_start = models.DateTimeField(verbose_name=_('дата старта'))
    date_end = models.DateTimeField(verbose_name=_('дата окончания'))
    description = models.TextField(verbose_name=_('Описание'))

    class Meta:
        db_table = 'poll'
        verbose_name = _('Опрос')
        verbose_name_plural = _('Опросы')

    def __str__(self):
        return self.name


class Question(models.Model):
    class Type:
        TEXT = 'Текст'
        CHOICE = 'Ответ с выбором одного варианта'
        MULTICHOICE = 'Ответ с выбором нескольких вариантов'

        choices = (
            (TEXT, 'Текст'),
            (CHOICE, 'Ответ с выбором одного варианта'),
            (MULTICHOICE, 'Ответ с выбором нескольких вариантов'),
        )

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='questions', verbose_name=_('Вопрос опроса'))
    question = models.TextField(verbose_name=_('Текст'))
    type = models.CharField(max_length=100, choices=Type.choices, default=Type.TEXT, verbose_name=_("Тип"))

    class Meta:
        db_table = 'question'
        verbose_name = _('Вопрос')
        verbose_name_plural = _('Вопросы')

    def __str__(self):
        return self.question


class Answer(models.Model):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name='user', null=True, blank=True)
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.CASCADE, verbose_name=_('Вопрос'))
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'answer'
        verbose_name = _('Ответ')
        verbose_name_plural = _('Ответы')

    def __str__(self):
        return self.value
