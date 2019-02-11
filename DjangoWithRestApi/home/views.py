from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "index.html"

class InnerPageView(TemplateView):
    template_name="content.html"

class TestPageView(TemplateView):
    template_name="test.html"