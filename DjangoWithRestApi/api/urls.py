from django.urls import path
from . import views
from . views import *


urlpatterns = [

    path('',views.QuoteAPIView.as_view(),name="quote_api_view"),
    path('quote/',views.QuoteAPIView.as_view(),name="quote_api_view2"),
    path('quote_category/',views.QuoteCategoryAPIView.as_view(),name="Quote_category_api_view"),
    path('quote/<int:pk>/',QuoteAPIDetailView.as_view()),
    path('quote/new/', QuoteAPINewView.as_view()),

    path('quote_category/<int:pk>/', views.QuoteCategoryAPIDetailView.as_view()),
    path('quote_category/new/', views.QuoteCategoryAPINewView.as_view()),



]