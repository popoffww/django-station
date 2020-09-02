from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import City
from .forms import CityForm

def home(request):
    if request.method == 'POST':
        form = CityForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
    form = CityForm()
    city = request.POST.get('name')
    cities = City.objects.all()
    return render(request, 'cities/home.html', {'objects_list': cities, 'form': form})

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
