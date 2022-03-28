from django.shortcuts import render
from django.http import HttpResponse
from .models import Sons


# Create your views here.
def index(request):
     '''
     sons = Sons.objects.all()
     sons_title = [sons.titre for sons in sons]
     sons_title_str = ", ".join(sons_title)
     return HttpResponse("Mes sons : " + sons_title_str)'''
     sons = Sons.objects.all().order_by('date')
     return render(request, 'menu/index.html', {'sons': sons})