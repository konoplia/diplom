from django.urls import path
from .views import cinema  # CinemaListView

urlpatterns = [
    path('', cinema, name='cinema_list')
    # path('', CinemaListView.as_view(), name='cinema_list'),
]
