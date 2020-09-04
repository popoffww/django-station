from django.urls import path
from .views import home
from .views import TrainCreateView

urlpatterns = [
    path('', home, name='home'),
    # path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    # path('update/<int:pk>/', CityUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>/', CityDeleteView.as_view(), name='delete'),
    path('add/', TrainCreateView.as_view(), name='add'),
]