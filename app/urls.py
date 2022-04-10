from django.urls import path, include

from app import conf

from app.views.cantina_view import ListInitial

urlpatterns = []

urlpatterns += [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls'))
]

from app.views import tipo_item

urlpatterns += [
    # tipo_item
    path(
        'tipoitem/',
        tipo_item.List.as_view(),
        name=conf.TIPOITEM_LIST_URL_NAME
    ),
    path(
        'tipoitem/full/',
        tipo_item.ListFull.as_view(),
        name='TIPOITEM_list_full'
    ),
    path(
        'tipoitem/create/',
        tipo_item.Create.as_view(),
        name=conf.TIPOITEM_CREATE_URL_NAME
    ),
    path(
        'tipoitem/<int:pk>/',
        tipo_item.Detail.as_view(),
        name=conf.TIPOITEM_DETAIL_URL_NAME
    ),
    path(
        'tipoitem/<int:pk>/update/',
        tipo_item.Update.as_view(),
        name=conf.TIPOITEM_UPDATE_URL_NAME
    ),
    path(
        'tipoitem/<int:pk>/delete/',
        tipo_item.Delete.as_view(),
        name=conf.TIPOITEM_DELETE_URL_NAME
    ),
    path(
        'tipoitem/list/json/',
        tipo_item.TipoItemListJson.as_view(),
        name=conf.TIPOITEM_LIST_JSON_URL_NAME
    )
]

from app.views import item

urlpatterns += [
    # item
    path(
        'item/',
        item.List.as_view(),
        name=conf.ITEM_LIST_URL_NAME
    ),
    path(
        'item/full/',
        item.ListFull.as_view(),
        name='ITEM_list_full'
    ),
    path(
        'item/create/',
        item.Create.as_view(),
        name=conf.ITEM_CREATE_URL_NAME
    ),
    path(
        'item/<int:pk>/',
        item.Detail.as_view(),
        name=conf.ITEM_DETAIL_URL_NAME
    ),
    path(
        'item/<int:pk>/update/',
        item.Update.as_view(),
        name=conf.ITEM_UPDATE_URL_NAME
    ),
    path(
        'item/<int:pk>/delete/',
        item.Delete.as_view(),
        name=conf.ITEM_DELETE_URL_NAME
    ),
    path(
        'item/list/json/',
        item.ItemListJson.as_view(),
        name=conf.ITEM_LIST_JSON_URL_NAME
    )
]

from app.views import pedido

urlpatterns += [
    # pedido
    path(
        'pedido/',
        pedido.List.as_view(),
        name=conf.PEDIDO_LIST_URL_NAME
    ),
    path(
        'pedido/full/',
        pedido.ListFull.as_view(),
        name='PEDIDO_list_full'
    ),
    path(
        'pedido/create/',
        pedido.Create.as_view(),
        name=conf.PEDIDO_CREATE_URL_NAME
    ),
    path(
        'pedido/<int:pk>/',
        pedido.Detail.as_view(),
        name=conf.PEDIDO_DETAIL_URL_NAME
    ),
    path(
        'pedido/<int:pk>/update/',
        pedido.Update.as_view(),
        name=conf.PEDIDO_UPDATE_URL_NAME
    ),
    path(
        'pedido/<int:pk>/delete/',
        pedido.Delete.as_view(),
        name=conf.PEDIDO_DELETE_URL_NAME
    ),
    path(
        'pedido/list/json/',
        pedido.PedidoListJson.as_view(),
        name=conf.PEDIDO_LIST_JSON_URL_NAME
    )
]

from app.views import item_pedido

urlpatterns += [
    # item_pedido
    path(
        'itempedido/',
        item_pedido.List.as_view(),
        name=conf.ITEMPEDIDO_LIST_URL_NAME
    ),
    path(
        'itempedido/full/',
        item_pedido.ListFull.as_view(),
        name='ITEMPEDIDO_list_full'
    ),
    path(
        'itempedido/create/',
        item_pedido.Create.as_view(),
        name=conf.ITEMPEDIDO_CREATE_URL_NAME
    ),
    path(
        'itempedido/<int:pk>/',
        item_pedido.Detail.as_view(),
        name=conf.ITEMPEDIDO_DETAIL_URL_NAME
    ),
    path(
        'itempedido/<int:pk>/update/',
        item_pedido.Update.as_view(),
        name=conf.ITEMPEDIDO_UPDATE_URL_NAME
    ),
    path(
        'itempedido/<int:pk>/delete/',
        item_pedido.Delete.as_view(),
        name=conf.ITEMPEDIDO_DELETE_URL_NAME
    ),
    path(
        'itempedido/list/json/',
        item_pedido.ItemPedidoListJson.as_view(),
        name=conf.ITEMPEDIDO_LIST_JSON_URL_NAME
    )
]

urlpatterns += [
    path(
        '',
        ListInitial.as_view(),
        name='index'
    ),
]
