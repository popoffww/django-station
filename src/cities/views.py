from django.shortcuts import render
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import City
from .forms import CityForm

def home(request):
    cities = City.objects.all()
    paginator = Paginator(cities, 3)
    page_number = request.GET.get('page')
    cities = paginator.get_page(page_number)
    return render(request, 'cities/home.html', {'objects_list': cities})

class CityDetailView(DetailView):
    queryset = City.objects.all()
    context_object_name = 'object'
    template_name = 'cities/detail.html'

class CityCreateView(CreateView):
    model= City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('city:home')

class CityUpdateView(UpdateView):
    model= City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('city:home')

class CityDeleteView(DeleteView):
    model= City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('city:home')

    # Удаление без использования template_name
    # Удаляет не спрашивая

    # def get(self, request, *args, **kwargs):
    #     return self.post(request, *args, **kwargs)
