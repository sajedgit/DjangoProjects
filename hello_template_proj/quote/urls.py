from django.urls import path
from . import views

urlpatterns = [

    path('quote/',views.QuoteView.as_view(),name="quote")
]