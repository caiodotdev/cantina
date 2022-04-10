from rest_framework import serializers


from app.models import TipoItem
class TipoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoItem
        fields = ("id", "nome")


from app.models import Item
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("id", "tipo", "nome", "img", "qtd_total", "valor")


from app.models import Pedido
class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ("id", "cliente", "total", "tipo_pgto", "status")


from app.models import ItemPedido
class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = ("id", "pedido", "item", "qtd", "total")


