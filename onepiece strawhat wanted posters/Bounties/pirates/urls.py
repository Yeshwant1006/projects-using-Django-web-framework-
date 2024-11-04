from django.urls import path
from .views import PirateListView, PirateDetailView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('pirates/', PirateListView.as_view(), name='pirate_list'),
    path('pirates/<int:pk>/', PirateDetailView.as_view(), name='pirate_detail'),
]

