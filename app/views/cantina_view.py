from django.views.generic import ListView

from app.models import Item, Caixa


class ListInitial(ListView):
    login_url = '/admin/login/'
    template_name = 'cantina_templates/list.html'
    model = Item
    context_object_name = 'items'
    ordering = '-id'
    paginate_by = 10

    def custo_items(self):
        qs = Item.objects.all()
        total = 0
        for item in qs:
            total = total + (item.valor_custo * item.qtd_inicial)
        return total

    def calc_lucro(self, caixa):
        total = caixa.valor_total - caixa.valor_inicial
        return total - self.custo_items()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListInitial, self).get_context_data(**kwargs)
        caixa = Caixa.objects.first()
        context['caixa'] = caixa
        context['lucro'] = self.calc_lucro(caixa)
        return context
