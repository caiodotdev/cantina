#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.admin.utils import NestedObjects
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import FieldDoesNotExist
from django.db import transaction
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView, DeleteView, UpdateView
)
from django.views.generic.list import ListView

from django.db.models import Q


try:
    from django.core.urlresolvers import reverse_lazy
except ImportError:
    from django.urls import reverse_lazy, reverse

from app.models import Item
from app.forms import ItemForm, ItemPedidoItemFormSet
from app.mixins import ItemMixin
from app.conf import ITEM_DETAIL_URL_NAME, ITEM_LIST_URL_NAME

from django_datatables_view.base_datatable_view import BaseDatatableView

from app.utils import upload_image, upload_file

import django_filters

class ItemFormSetManagement(object):
    formsets = [ItemPedidoItemFormSet]

    def form_valid(self, form):
        context = self.get_context_data()
        with transaction.atomic():
            self.object = form.save()
            
            for Formset in self.formsets:
                formset = context["{}set".format(str(Formset.model.__name__).lower())]
                if formset.is_valid():
                    formset.instance = self.object
                    formset.save()
        return super(ItemFormSetManagement, self).form_valid(form)

    def get_context_data(self, **kwargs):
        data = super(ItemFormSetManagement, self).get_context_data(**kwargs)
        for Formset in self.formsets:
            if self.request.POST:
                data["{}set".format(str(Formset.model.__name__).lower())] = Formset(self.request.POST,
                                                                                    self.request.FILES,
                                                                                    instance=self.object)
            else:
                data["{}set".format(str(Formset.model.__name__).lower())] = Formset(instance=self.object)
        return data


class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = Item
        fields = ["id", "tipo__nome", "nome", "img", "qtd_total","valor_custo",  "valor_final"]


class List(LoginRequiredMixin, ItemMixin, ListView):
    """
    List all Items
    """
    login_url = '/admin/login/'
    template_name = 'item/list.html'
    model = Item
    context_object_name = 'items'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)
        queryset = self.get_queryset()
        filter = ItemFilter(self.request.GET, queryset)
        context["filter"] = filter
        return context


class ListFull(LoginRequiredMixin, ItemMixin, ListView):
    """
    List all Items
    """
    login_url = '/admin/login/'
    template_name = 'item/list_full.html'
    model = Item
    context_object_name = 'items'
    ordering = '-id'
    paginate_by = 10
    search = ''

    def get_queryset(self):
        queryset = super().get_queryset()
        filter =  ItemFilter(self.request.GET, queryset)
        queryset = self.search_general(filter.qs)
        queryset = self.ordering_data(queryset)
        return queryset

    def search_general(self, qs):
        if 'search' in self.request.GET:
            self.search = self.request.GET['search']
            if self.search:
                search = self.search
                qs = qs.filter(Q(id__icontains=search)| Q(tipo__nome__icontains=search)| Q(nome__icontains=search)| Q(img__icontains=search)| Q(qtd_total__icontains=search)| Q(valor__icontains=search))
        return qs

    def get_ordering(self):
        if 'ordering' in self.request.GET:
            self.ordering = self.request.GET['ordering']
            if self.ordering:
                return self.ordering
            else:
                self.ordering = '-id'
        return self.ordering

    def ordering_data(self, qs):
        qs = qs.order_by(self.get_ordering())
        return qs

    def get_context_data(self, **kwargs):
        context = super(ListFull, self).get_context_data(**kwargs)
        queryset = self.get_queryset()
        filter = ItemFilter(self.request.GET, queryset)
        page_size = self.get_paginate_by(queryset)
        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
            context.update(**{
                'ordering': self.ordering,
                'search': self.search,
                'filter': filter,
                'paginator': paginator,
                'page_obj': page,
                'is_paginated': is_paginated,
                'object_list': queryset
            })
        else:
            context.update(**{
                'search': self.search,
                'ordering': self.ordering,
                'filter': filter,
                'paginator': None,
                'page_obj': None,
                'is_paginated': False,
                'object_list': queryset
            })
        return context


class Create(LoginRequiredMixin, ItemMixin, PermissionRequiredMixin, ItemFormSetManagement, CreateView):
    """
    Create a Item
    """
    login_url = '/admin/login/'
    model = Item
    permission_required = (
        'app.add_item'
    )
    form_class = ItemForm
    template_name = 'item/create.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super(Create, self).get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy(ITEM_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())

    def get_initial(self):
        data = super(Create, self).get_initial()
        return data

    def form_valid(self, form):
        messages.success(self.request, 'Item criado com sucesso')
        return super(Create, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Houve algum erro, tente novamente')
        return super(Create, self).form_invalid(form)


class Detail(LoginRequiredMixin, ItemMixin, DetailView):
    """
    Detail of a Item
    """
    login_url = '/admin/login/'
    model = Item
    template_name = 'item/detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)
        return context


class Update(LoginRequiredMixin, ItemMixin, PermissionRequiredMixin, ItemFormSetManagement, UpdateView):
    """
    Update a Item
    """
    login_url = '/admin/login/'
    model = Item
    template_name = 'item/update.html'
    context_object_name = 'item'
    form_class = ItemForm
    permission_required = (
        'app.change_item'
    )

    def get_initial(self):
        data = super(Update, self).get_initial()
        return data

    def get_success_url(self):
        return reverse_lazy(ITEM_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())

    def get_context_data(self, **kwargs):
        data = super(Update, self).get_context_data(**kwargs)
        return data

    def form_valid(self, form):
        messages.success(self.request, 'Item atualizado com sucesso')
        return super(Update, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Houve algum erro, tente novamente')
        return super(Update, self).form_invalid(form)


class Delete(LoginRequiredMixin, ItemMixin, PermissionRequiredMixin, DeleteView):
    """
    Delete a Item
    """
    login_url = '/admin/login/'
    model = Item
    permission_required = (
        'app.delete_item'
    )
    template_name = 'item/delete.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super(Delete, self).get_context_data(**kwargs)
        collector = NestedObjects(using='default')
        collector.collect([self.get_object()])
        context['deleted_objects'] = collector.nested()
        return context

    def __init__(self):
        super(Delete, self).__init__()

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Item removido com sucesso')
        return super(Delete, self).delete(self.request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy(ITEM_LIST_URL_NAME)


class ItemListJson(BaseDatatableView):
    model = Item
    columns = ("id", "tipo", "nome", "img", "qtd_total", "valor_final")
    order_columns = ["id", "tipo__nome", "nome", "img", "qtd_total", "valor_final"]
    max_display_length = 500

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(Q(id__icontains=search)| Q(tipo__nome__icontains=search)| Q(nome__icontains=search)| Q(img__icontains=search)| Q(qtd_total__icontains=search)| Q(valor__icontains=search))
        filter = ItemFilter(self.request.GET, qs)
        return filter.qs
