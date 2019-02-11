from django.urls import path
from . import views

urlpatterns = [
    path('',views.BootstrapView.as_view(),name="bootstrap_view")
]
