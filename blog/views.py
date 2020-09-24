from django.shortcuts import render, get_object_or_404
from .models import Bottles
from django.utils import timezone

# Create your views here.
def bottle_list(request):
    bottles = Bottles.objects.filter(registered_date__lte=timezone.now()).order_by('-registered_date')
    return render(request, 'blog/bottle_list.html', {'bottles' : bottles})

def bottle_detail(request, pk):
    bottle = get_object_or_404(Bottles, pk=pk)
    return render(request, 'blog/bottle_detail.html', {'bottle': bottle})

def bottle_search(request):
    form = SearchForm()
    return render(request, 'blog/chemical_search.html', {'form': form})