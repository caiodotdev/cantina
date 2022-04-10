from django import forms
from django.forms import ModelForm, inlineformset_factory
from app.utils import generate_bootstrap_widgets_for_all_fields

from . import (
    models
)

class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # field.widget.attrs['class'] = 'form-control'
            if field_name == 'phone' or field_name == 'telefone':
                field.widget.attrs['class'] = 'form-control telefone phone'
            if field_name == 'cep' or field_name == 'postalcode':
                field.widget.attrs['class'] = 'form-control cep'


class TipoItemForm(BaseForm, ModelForm):
    class Meta:
        model = models.TipoItem
        fields = ("id", "nome")
        widgets = generate_bootstrap_widgets_for_all_fields(models.TipoItem)

    def __init__(self, *args, **kwargs):
        super(TipoItemForm, self).__init__(*args, **kwargs)


class TipoItemFormToInline(BaseForm, ModelForm):
    class Meta:
        model = models.TipoItem
        fields = ("id", "nome")
        widgets = generate_bootstrap_widgets_for_all_fields(models.TipoItem)

    def __init__(self, *args, **kwargs):
        super(TipoItemFormToInline, self).__init__(*args, **kwargs)



class ItemForm(BaseForm, ModelForm):
    class Meta:
        model = models.Item
        fields = ("id", "tipo", "nome", "img", "qtd_total", "valor")
        widgets = generate_bootstrap_widgets_for_all_fields(models.Item)

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)


class ItemFormToInline(BaseForm, ModelForm):
    class Meta:
        model = models.Item
        fields = ("id", "tipo", "nome", "img", "qtd_total", "valor")
        widgets = generate_bootstrap_widgets_for_all_fields(models.Item)

    def __init__(self, *args, **kwargs):
        super(ItemFormToInline, self).__init__(*args, **kwargs)


ItemTipoItemFormSet = inlineformset_factory(models.TipoItem, models.Item, form=ItemFormToInline, extra=1)


class PedidoForm(BaseForm, ModelForm):
    class Meta:
        model = models.Pedido
        fields = ("id", "cliente", "total", "tipo_pgto", "status")
        widgets = generate_bootstrap_widgets_for_all_fields(models.Pedido)

    def __init__(self, *args, **kwargs):
        super(PedidoForm, self).__init__(*args, **kwargs)


class PedidoFormToInline(BaseForm, ModelForm):
    class Meta:
        model = models.Pedido
        fields = ("id", "cliente", "total", "tipo_pgto", "status")
        widgets = generate_bootstrap_widgets_for_all_fields(models.Pedido)

    def __init__(self, *args, **kwargs):
        super(PedidoFormToInline, self).__init__(*args, **kwargs)



class ItemPedidoForm(BaseForm, ModelForm):
    class Meta:
        model = models.ItemPedido
        fields = ("id", "pedido", "item", "qtd", "total")
        widgets = generate_bootstrap_widgets_for_all_fields(models.ItemPedido)

    def __init__(self, *args, **kwargs):
        super(ItemPedidoForm, self).__init__(*args, **kwargs)


class ItemPedidoFormToInline(BaseForm, ModelForm):
    class Meta:
        model = models.ItemPedido
        fields = ("id", "pedido", "item", "qtd", "total")
        widgets = generate_bootstrap_widgets_for_all_fields(models.ItemPedido)

    def __init__(self, *args, **kwargs):
        super(ItemPedidoFormToInline, self).__init__(*args, **kwargs)


ItemPedidoPedidoFormSet = inlineformset_factory(models.Pedido, models.ItemPedido, form=ItemPedidoFormToInline, extra=1)

ItemPedidoItemFormSet = inlineformset_factory(models.Item, models.ItemPedido, form=ItemPedidoFormToInline, extra=1)
