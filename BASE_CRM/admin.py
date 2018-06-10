from django.contrib import admin
from models import *


class Contact_typesAdmin(admin.ModelAdmin):
    list_display = ['type']
    ordering = ['-id']


class StagesAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['-id']


class SourcesAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['-id']


class Product_groupsAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['-id']


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'date_create']
    ordering = ['-id']


class CustomersAdmin(admin.ModelAdmin):
    # list_display = ['name', 'role', 'date_create']
    ordering = ['-id']


class ContactsAdmin(admin.ModelAdmin):
    list_display = ['user', 'type', 'contact', 'date_create']
    ordering = ['-user', '-id']


class Deal_stagesAdmin(admin.ModelAdmin):
    list_display = ['stage', 'date_open', 'date_close']
    ordering = ['-date_close', '-date_open']


class DealsAdmin(admin.ModelAdmin):
    list_display = ['customer', 'product', 'source', 'deal_stage', 'date_open', 'date_close']
    ordering = ['-id']


admin.site.register(Contact_types, Contact_typesAdmin)
admin.site.register(Stages, StagesAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Customers, CustomersAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Deal_stages, Deal_stagesAdmin)
admin.site.register(Deals, DealsAdmin)
admin.site.register(Product_groups, Product_groupsAdmin)
admin.site.register(Sources, SourcesAdmin)