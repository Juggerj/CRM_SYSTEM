# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Contact_types(models.Model):
    type = models.CharField(verbose_name='Тип контакта', max_length=30)

    def __unicode__(self):
        return self.type

    class Meta:
        verbose_name = 'Тип контакта'
        verbose_name_plural = 'Типы контактов'


class Stages(models.Model):
    name = models.CharField(verbose_name='Название', max_length=127)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Стадия сделки'
        verbose_name_plural = 'Справочник стадий сделок'


class Product_groups(models.Model):
    name = models.CharField(verbose_name='Название', max_length=127)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа продуктов'
        verbose_name_plural = 'Группы продуктов'


class Products(models.Model):
    product_group = models.ForeignKey(Product_groups, verbose_name='Группа продукта', blank=True, null=True)
    name = models.CharField(verbose_name='Название', max_length=127)
    price = models.IntegerField(verbose_name='Стоимость')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Customers(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=191)
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'


class Contacts(models.Model):
    user = models.ForeignKey(Customers, verbose_name='Пользователь')
    type = models.ForeignKey(Contact_types, verbose_name='Тип контакта')
    contact = models.CharField(verbose_name='Контакт', max_length=191)
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __unicode__(self):
        return self.user.name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Deal_stages(models.Model):
    stage = models.ForeignKey(Stages, verbose_name='Стадия')
    date_open = models.DateTimeField(auto_now_add=True, verbose_name='Дата открытия')
    date_close = models.DateTimeField(verbose_name='Дата закрытия', blank=True, null=True)
    comments = models.TextField(verbose_name='Комментарий', max_length=2000, blank=True, null=True)

    def __unicode__(self):
        return self.stage.name

    class Meta:
        verbose_name = 'Стадия сделки'
        verbose_name_plural = 'Стадии сделок'


class Sources(models.Model):
    name = models.CharField(verbose_name='Исчтоник', max_length=127)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Источник сделки'
        verbose_name_plural = 'Источники сделок'


class Deals(models.Model):
    customer = models.ForeignKey(Customers, verbose_name='Покупатель')
    manager = models.ForeignKey(User, verbose_name='Менеджер')
    product = models.ForeignKey(Products, verbose_name='Продукт')
    deal_stage = models.ForeignKey(Deal_stages, verbose_name='Стадия сделки')
    date_open = models.DateTimeField(auto_now_add=True, verbose_name='Дата открытия')
    date_close = models.DateTimeField(verbose_name='Дата закрытия', blank=True, null=True)
    comments = models.TextField(verbose_name='Комментарий', max_length=2000, blank=True, null=True)
    source = models.ForeignKey(Sources, verbose_name='Источник сделки', blank=True, null=True)

    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'