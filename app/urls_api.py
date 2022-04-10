from rest_framework.routers import DefaultRouter
from app import (
    viewsets
)

api_urlpatterns = []

tipoitem_router = DefaultRouter()

tipoitem_router.register(
    r'^api/tipoitem',
    viewsets.TipoItemViewSet,
    basename="tipoitem"
)

api_urlpatterns += tipoitem_router.urls
item_router = DefaultRouter()

item_router.register(
    r'^api/item',
    viewsets.ItemViewSet,
    basename="item"
)

api_urlpatterns += item_router.urls
pedido_router = DefaultRouter()

pedido_router.register(
    r'^api/pedido',
    viewsets.PedidoViewSet,
    basename="pedido"
)

api_urlpatterns += pedido_router.urls
itempedido_router = DefaultRouter()

itempedido_router.register(
    r'^api/itempedido',
    viewsets.ItemPedidoViewSet,
    basename="itempedido"
)

api_urlpatterns += itempedido_router.urls
