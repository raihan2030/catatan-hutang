from django.shortcuts import render
from .models import CatatanHutang

# Create your views here.
def home(request):
  data = {
    'title': 'Beranda',
    'hutang': CatatanHutang.objects.all()
  }

  return render(request, 'home.html', data)
