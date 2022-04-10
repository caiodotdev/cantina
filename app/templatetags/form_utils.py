from django import template
from django.template.loader import get_template

from app.models import Pedido, TipoPagamento

register = template.Library()


@register.filter()
def total_vendidos(qs):
    total = 0
    for item in qs:
        vendidos_item = count_vendidos(item.itempedido_set.all())
        total = total + vendidos_item
    return total


@register.filter()
def total_restantes(qs):
    total = 0
    for item in qs:
        total = total + item.qtd_total
    return total


@register.filter()
def total_pct_vendidos(qs):
    vendidos = total_vendidos(qs)
    if vendidos:
        total_initial = vendidos + total_restantes(qs)
        return int(vendidos * 100 / total_initial)
    return 0


@register.filter()
def total_amount_vendidos(qs):
    return "{:.2f}".format(float(total_vendidos(qs) * 4.5))


@register.filter()
def total_pct_restantes(qs):
    vendidos = total_vendidos(qs)
    restantes = total_restantes(qs)
    if restantes:
        total_initial = vendidos + restantes
        return int(restantes * 100 / total_initial)
    return 0


@register.filter()
def total_amount_restantes(qs):
    return "{:.2f}".format(float(total_restantes(qs) * 4.5))


@register.filter()
def total_amount_pix(qs):
    total = 0
    for pedido in Pedido.objects.filter(tipo_pgto=TipoPagamento.PIX):
        total = total + pedido.total
    return total


@register.filter()
def total_amount_dinheiro(qs):
    total = 0
    for pedido in Pedido.objects.filter(tipo_pgto=TipoPagamento.DINHEIRO):
        total = total + pedido.total
    return total


@register.filter()
def count_vendidos(qs):
    qtd_vendidos = 0
    for itempedido in qs:
        qtd_vendidos = qtd_vendidos + itempedido.qtd
    return qtd_vendidos


@register.filter()
def get_fields(obj):
    return [(field.name, field.value_to_string(obj)) for field in obj._meta.fields]


@register.filter("add_formset_element")
def add_formset_element_js(formset):
    # We just use the first column
    if len(formset) > 0:
        row = formset[0]
        for input in row:
            tokens = input.html_name.split("-")
            new_text = ""
            for token in tokens:
                new_token_text = ""
                try:
                    int(token)
                    new_token_text = "{{id}}"
                except ValueError:
                    new_token_text = token
                new_text += new_token_text + "-"
            new_text = new_text[:-1]
            input.html_name = new_text
        return get_template("base/add_formset_underscore.html").render({"form": row})
    return ""


@register.simple_tag(name="formset_js")
def formset_js():
    return get_template("base/add_formset_underscore_js.html").render()
