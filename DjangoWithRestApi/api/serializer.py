from rest_framework import serializers

from quote.models import Quote
from quote.models import QuoteCategory


class QuoteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=QuoteCategory
        # ('__all__') for all field
        # ['title']
        fields=('__all__')


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model:Quote
        # ('__all__') for all field
        # fields=['quote','author']
        fields=('__all__')


