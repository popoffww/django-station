from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Train
from .forms import TrainForm

def home(request):
    trains = Train.objects.all()
    paginator = Paginator(trains, 3)
    page_number = request.GET.get('page')
    trains = paginator.get_page(page_number)
    return render(request, 'trains/home.html', {'objects_list': trains})

class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    context_object_name = 'object'
    template_name = 'trains/detail.html'

class TrainCreateView(SuccessMessageMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('train:home')
    success_message = 'Маршрут успешно создан'

class TrainUpdateView(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('train:home')
    success_message = 'Маршрут успешно изменен'

class TrainDeleteView(DeleteView):
    model= Train
    template_name = 'trains/delete.html'
    success_url = reverse_lazy('train:home')