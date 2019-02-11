from django.urls import path
from . import views

urlpatterns = [

    path('',views.HomeView.as_view(),name="home_view"),
    path('innerPage/',views.InnerPageView.as_view(),name="inner_view"),
    path('testPage/',views.TestPageView.as_view(),name="testPage_view")
]
