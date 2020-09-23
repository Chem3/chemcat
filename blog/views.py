from django.shortcuts import render
from .models import Bottles
from django.utils import timezone

# Create your views here.
def bottle_list(request):
    bottles = Bottles.objects.filter(registered_date__lte=timezone.now()).order_by('-registered_date')
    return render(request, 'blog/bottle_list.html', {'bottles' : bottles})