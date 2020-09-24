from django.shortcuts import render, get_object_or_404
from .models import Bottles
from django.utils import timezone
from django.views.generic import TemplateView, ListView
from django.db.models import Q

# Create your views here.
def bottle_list(request):
    bottles = Bottles.objects.filter(registered_date__lte=timezone.now()).order_by('-registered_date')[:20]
    return render(request, 'blog/bottle_list.html', {'bottles' : bottles})

def bottle_detail(request, pk):
    bottle = get_object_or_404(Bottles, pk=pk)
    return render(request, 'blog/bottle_detail.html', {'bottle': bottle})

class SearchResultsView(ListView):
    model = Bottles
    template_name = 'blog/bottle_search.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Bottles.objects.filter(
            Q(product_name__icontains=query) |
            Q(barcode__icontains=query)
        )
        return object_list