from rest_framework import generics,permissions

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


class QuoteAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteAPINewView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Quote.objects.all().order_by('-id')[:1]
    serializer_class = QuoteSerializer
    

#  for Quote Category  get,update and delete
class QuoteCategoryAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuoteCategory.objects.all()
    serializer_class = QuoteCategorySerializer

#  for Quote Category  add new
class QuoteCategoryAPINewView(generics.ListCreateAPIView):
    queryset = QuoteCategory.objects.all().order_by('-id')[:1]
    serializer_class = QuoteCategorySerializer
