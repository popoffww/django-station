from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Train
# from .forms import TrainForm

def home(request):
    trains = Train.objects.all()
    paginator = Paginator(trains, 3)
    page_number = request.GET.get('page')
    trains = paginator.get_page(page_number)
    return render(request, 'trains/home.html', {'objects_list': trains})
