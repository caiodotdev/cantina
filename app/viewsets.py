from rest_framework import viewsets

from django_filters import rest_framework as filters

from . import (
    serializers,
    models
)

import django_filters



class TipoItemFilter(django_filters.FilterSet):
    class Meta:
        model = models.TipoItem
        fields = ["id", "nome"]


class TipoItemViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.TipoItemSerializer
    queryset = models.TipoItem.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TipoItemFilter



class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = models.Item
        fields = ["id", "tipo__nome", "nome", "img", "qtd_total", "valor"]


class ItemViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.ItemSerializer
    queryset = models.Item.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ItemFilter



class PedidoFilter(django_filters.FilterSet):
    class Meta:
        model = models.Pedido
        fields = ["id", "cliente", "total", "tipo_pgto", "status"]


class PedidoViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.PedidoSerializer
    queryset = models.Pedido.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PedidoFilter



class ItemPedidoFilter(django_filters.FilterSet):
    class Meta:
        model = models.ItemPedido
        fields = ["id", "pedido__cliente", "item__id", "qtd", "total"]


class ItemPedidoViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.ItemPedidoSerializer
    queryset = models.ItemPedido.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ItemPedidoFilter

