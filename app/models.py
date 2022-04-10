from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.

# Create your models here.
from djmoney.models.fields import MoneyField


class TimeStamped(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)


class TipoItem(TimeStamped):
    nome = models.CharField(max_length=255, blank=True, null=True, default='Salgado')

    def __str__(self):
        return str(self.nome)


class TipoPagamento(models.IntegerChoices):
    """
    Enum for status of a task.
    """
    DINHEIRO = 0, 'Dinheiro'
    PIX = 1, 'PIX'
    CREDITO = 2, 'Cartao Credito'
    DEBITO = 3, 'Debito'


class StatusPedido(models.IntegerChoices):
    """
    Enum for status of a task.
    """
    ABERTO = 0, 'ABERTO'
    FECHADO = 1, 'FECHADO'


class Item(TimeStamped):
    tipo = models.ForeignKey(TipoItem, blank=True, null=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    img = models.URLField(blank=True, null=True)
    qtd_total = models.IntegerField(default=0, validators=[
        MaxValueValidator(500),
        MinValueValidator(0)
    ])
    qtd_inicial = models.IntegerField(default=0, validators=[
        MaxValueValidator(500),
        MinValueValidator(0)
    ])
    valor_custo = MoneyField(max_digits=14, decimal_places=2, default_currency='BRL', blank=True, null=True)
    valor_final = MoneyField(max_digits=14, decimal_places=2, default_currency='BRL')

    def __str__(self):
        return "%s" % self.nome



class Caixa(TimeStamped):
    valor_inicial = MoneyField(max_digits=14, decimal_places=2, default_currency='BRL', blank=True, null=True)
    valor_total = MoneyField(max_digits=14, decimal_places=2, default_currency='BRL', blank=True, null=True)


class Pedido(TimeStamped):
    cliente = models.CharField(max_length=255, blank=True, null=True, default='Cliente')
    total = MoneyField(max_digits=14, decimal_places=2, default_currency='BRL', blank=True, null=True)
    tipo_pgto = models.IntegerField(choices=TipoPagamento.choices,
                                    default=TipoPagamento.PIX)
    status = models.IntegerField(choices=StatusPedido.choices,
                                 default=StatusPedido.ABERTO)

    def __str__(self):
        return "%s - %s" % (self.cliente, str(self.total))

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        total = 0
        for item in self.itempedido_set.all():
            total = total + item.total
        self.total = total
        self.status = StatusPedido.FECHADO

        super(Pedido, self).save()


class ItemPedido(TimeStamped):
    pedido = models.ForeignKey(Pedido, blank=True, null=True, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.CASCADE)
    qtd = models.IntegerField(blank=True, null=True, default=0)
    total = MoneyField(max_digits=14, decimal_places=2, default_currency='BRL', blank=True, null=True)

    def __str__(self):
        return "%s - %s - %s" % (self.item, str(self.qtd), str(self.total))

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        item = self.item
        self.total = item.valor_final * self.qtd
        item.qtd_total = item.qtd_total - self.qtd
        item.save()
        return super(ItemPedido, self).save(force_insert=False, force_update=False, using=None,
                                            update_fields=None)


# Abrir Pedido (listagem sem select de itens) - (nome, tipo pgto) ->
# Select Item -> ItemPedidoForm w/ Pedido em context or param.
# Carrinho -> ver tabela -> fechar pedido ou continuar comprando
# encerra e abre (listagem sem select de itens)

