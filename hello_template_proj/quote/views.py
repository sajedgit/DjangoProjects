from django.views.generic import ListView

from . models import  QuoteCategory
from . models import  Quote

class QuoteView(ListView):
    template_name="quote.html"

    model = Quote

    def get_queryset(self):
        query_set=super().get_queryset()
        return  query_set.select_related('quote_category')



