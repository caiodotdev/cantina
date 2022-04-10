#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.apps import apps
from django.contrib import admin

# Register your models here.

from app.models import *


def approve_selected(modeladmin, request, queryset):
    queryset.update(is_approved=True)


def desapprove_selected(modeladmin, request, queryset):
    queryset.update(is_approved=False)


approve_selected.short_description = "Aprovar itens selecionados"
desapprove_selected.short_description = "Desaprovar itens selecionados"


class ItemInline(admin.TabularInline):
    model = Item



class TipoItemAdmin(admin.ModelAdmin):
    list_filter = []
    search_fields = (
        'id',
    )
    inlines = [ItemInline]
    list_display = ("id", "nome")

admin.site.register(TipoItem, TipoItemAdmin)


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido



class ItemAdmin(admin.ModelAdmin):
    list_filter = []
    search_fields = (
        'id',
    )
    inlines = [ItemPedidoInline]
    list_display = ("id", "tipo", "nome", "img", "qtd_total", "valor")

admin.site.register(Item, ItemAdmin)


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido



class PedidoAdmin(admin.ModelAdmin):
    list_filter = []
    search_fields = (
        'id',
    )
    inlines = [ItemPedidoInline]
    list_display = ("id", "cliente", "total", "tipo_pgto", "status")

admin.site.register(Pedido, PedidoAdmin)


class ItemPedidoAdmin(admin.ModelAdmin):
    list_filter = []
    search_fields = (
        'id',
    )
    inlines = []
    list_display = ("id", "pedido", "item", "qtd", "total")

admin.site.register(ItemPedido, ItemPedidoAdmin)
