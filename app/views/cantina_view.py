from django.views.generic import ListView

from app.models import Item


class ListInitial(ListView):
    login_url = '/admin/login/'
    template_name = 'cantina_templates/list.html'
    model = Item
    context_object_name = 'items'
    ordering = '-id'
    paginate_by = 10
