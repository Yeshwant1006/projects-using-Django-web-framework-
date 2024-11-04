from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView
from django.views import View  
from .models import Pirate

class PirateListView(View):
    def get(self, request):
        pirates = Pirate.objects.all()
        return render(request, 'pirates/pirate_list.html', {'pirates': pirates})

class HomeView(View):
    def get(self, request):
        return PirateListView.as_view()(request)

class PirateDetailView(DetailView):
    model = Pirate
    template_name = 'pirates/pirate_detail.html'
    context_object_name = 'pirate'

    def post(self, request, *args, **kwargs):
        pirate = self.get_object()
        return redirect('pirate_detail', pirate_id=pirate.id)


 









