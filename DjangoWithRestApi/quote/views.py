from django.views.generic import TemplateView

class QuoteView(TemplateView):
    template_name = "quote/index.html"
