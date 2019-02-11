from django.views.generic import TemplateView


class BootstrapView(TemplateView):
    template_name = 'index_bootstrap.html'
