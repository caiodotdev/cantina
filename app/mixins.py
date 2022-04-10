from app.models import (
    TipoItem
)
from django.core.exceptions import FieldDoesNotExist

class TipoItemMixin(object):

    def kwargs_for_reverse_url(self):
        kwargs_dict = dict()
        if self.model:
            self.object = self.object if self.object is not None else self.get_object()
            try:
                self.model._meta.get_field('slug')
                kwargs_dict['slug'] = self.object.slug
            except FieldDoesNotExist:
                kwargs_dict['pk'] = self.object.id
        return kwargs_dict

    def get_context_data(self, **kwargs):
        context = super(TipoItemMixin, self).get_context_data(**kwargs)
        if self.model:
            context['model_name'] = self.model._meta.verbose_name.title()
            context['model_name_plural'] = self.model._meta.verbose_name_plural.title()
        return context

    def get_tipoitem(self):
        return TipoItem.objects.get(pk=self.kwargs.get("pk_tipoitem", 0))

class ItemMixin(object):

    def kwargs_for_reverse_url(self):
        kwargs_dict = dict()
        if self.model:
            self.object = self.object if self.object is not None else self.get_object()
            try:
                self.model._meta.get_field('slug')
                kwargs_dict['slug'] = self.object.slug
            except FieldDoesNotExist:
                kwargs_dict['pk'] = self.object.id
        return kwargs_dict

    def get_context_data(self, **kwargs):
        context = super(ItemMixin, self).get_context_data(**kwargs)
        if self.model:
            context['model_name'] = self.model._meta.verbose_name.title()
            context['model_name_plural'] = self.model._meta.verbose_name_plural.title()
        return context

    def get_item(self):
        return Item.objects.get(pk=self.kwargs.get("pk_item", 0))

class PedidoMixin(object):

    def kwargs_for_reverse_url(self):
        kwargs_dict = dict()
        if self.model:
            self.object = self.object if self.object is not None else self.get_object()
            try:
                self.model._meta.get_field('slug')
                kwargs_dict['slug'] = self.object.slug
            except FieldDoesNotExist:
                kwargs_dict['pk'] = self.object.id
        return kwargs_dict

    def get_context_data(self, **kwargs):
        context = super(PedidoMixin, self).get_context_data(**kwargs)
        if self.model:
            context['model_name'] = self.model._meta.verbose_name.title()
            context['model_name_plural'] = self.model._meta.verbose_name_plural.title()
        return context

    def get_pedido(self):
        return Pedido.objects.get(pk=self.kwargs.get("pk_pedido", 0))

class ItemPedidoMixin(object):

    def kwargs_for_reverse_url(self):
        kwargs_dict = dict()
        if self.model:
            self.object = self.object if self.object is not None else self.get_object()
            try:
                self.model._meta.get_field('slug')
                kwargs_dict['slug'] = self.object.slug
            except FieldDoesNotExist:
                kwargs_dict['pk'] = self.object.id
        return kwargs_dict

    def get_context_data(self, **kwargs):
        context = super(ItemPedidoMixin, self).get_context_data(**kwargs)
        if self.model:
            context['model_name'] = self.model._meta.verbose_name.title()
            context['model_name_plural'] = self.model._meta.verbose_name_plural.title()
        return context

    def get_itempedido(self):
        return ItemPedido.objects.get(pk=self.kwargs.get("pk_itempedido", 0))

