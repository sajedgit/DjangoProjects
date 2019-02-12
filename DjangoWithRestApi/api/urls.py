from django.urls import path
from . import views

urlpatterns = [

    path('',views.QuoteAPIView.as_view(),name="quote_api_view"),
    path('quote/',views.QuoteAPIView.as_view(),name="quote_api_view"),
    path('quote_category/',views.QuoteCategoryAPIView.as_view(),name="Quote_category_api_view"),
]