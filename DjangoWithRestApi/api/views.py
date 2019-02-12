from rest_framework import generics

from quote.models import Quote
from quote.models import QuoteCategory

from .serializer import QuoteSerializer
from .serializer import QuoteCategorySerializer

class QuoteAPIView(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

class QuoteCategoryAPIView(generics.ListAPIView):
    queryset = QuoteCategory.objects.all()
    serializer_class = QuoteCategorySerializer
