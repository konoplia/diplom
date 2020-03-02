from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.


# class CinemaListView(ListView):
#     template_name = 'cinema_box_office/poster.html'

def cinema(request):
    return render(request, 'cinema_box_office/poster.html')