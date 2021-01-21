from django.shortcuts import render, get_object_or_404
from .models import Bottles, Cabinets, Chemicals, Properties, Shelves
from django.utils import timezone
from django.views.generic import TemplateView, ListView
from django.db.models import Q, F
from datetime import date, timedelta
import wikipedia as wiki
import chemicals as chem

# Create your views here.


def bottle_list(request):
    bottles = Bottles.objects.filter(registered_date__lte=timezone.now()).order_by('-registered_date')[:20]
    shelves = Shelves.objects.all();
    days = 365*2
    start_date = date.today()
    end_date = start_date + timedelta(days=days)
    old_bottles = Bottles.objects.exclude(registered_date__range=[start_date, end_date]).order_by('registered_date')[:10]
    return render(request, 'blog/bottle_list.html', {'bottles': bottles, 'shelves': shelves, 'old_bottles': old_bottles})


def bottle_detail(request, pk):
    bottle = get_object_or_404(Bottles, pk=pk)
    carc_list = chem.safety.Carcinogen(bottle.chemical.cas)
    carc_str = carc_list.values()
    stel = chem.safety.STEL(bottle.chemical.cas)
    autoign = chem.safety.T_autoignition(bottle.chemical.cas)
    flash = chem.safety.T_flash(bottle.chemical.cas)
    absskin = chem.safety.Skin(bottle.chemical.cas)
    ceiling = chem.safety.Ceiling(bottle.chemical.cas)
    mp = chem.Tm(bottle.chemical.cas)
    bp = chem.Tb(bottle.chemical.cas)
    try:
        mw = chem.identifiers.MW(bottle.chemical.cas)
    except ValueError:
        mw = 0
    except TypeError:
        mw = 0
    dp_moment = chem.dipole_moment(bottle.chemical.cas)
    logp = chem.logP(bottle.chemical.cas)
    wikisummary = ""
    try:
        wikisummary = wiki.summary(bottle.chemical.iupac_name)
    except wiki.PageError:
        wikisummary = ""
    except wiki.DisambiguationError:
        wikisummary = ""
    except wiki.RedirectError:
        wikisummary = ""
    return render(request, 'blog/bottle_detail.html',
                  {'bottle': bottle,'wiki': wikisummary,
                   'carcinogen': carc_str, 'stel': stel,
                   'autoign': autoign, 'flash': flash,
                   'absskin': absskin, 'ceiling':ceiling,
                   'mp':mp,'bp':bp,'mw':mw,'dp_moment':dp_moment,
                   'logp':logp})


def shelf_detail(request, shortname):
    shelf = get_object_or_404(Shelves, shortname__icontains=shortname)
    bottles = Bottles.objects.filter(shelf__shelf_id=shelf.shelf_id).order_by('-registered_date')
    properties = Properties.objects.all()
    labels = []
    data = []
    total_amount = 0
    for chem_property in properties:
        amount = 0
        labels.append(chem_property.property_name)
        for bottle in bottles:
            if bottle.chemical.property.property_name == chem_property.property_name:
                amount = amount + (bottle.amount / bottle.unit.si_conversion_factor)
        data.append(amount)
        total_amount += amount
    return render(request, 'blog/shelf_detail.html',
                  {'bottles': bottles, 'shelf': shelf, 'labels': labels, 'data': data, 'total': total_amount})


class SearchResultsView(ListView):
    model = Bottles
    template_name = 'blog/bottle_search.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Bottles.objects.filter(
            Q(product_name__icontains=query) |
            Q(chemical__iupac_name__icontains=query) |
            Q(barcode__icontains=query) |
            Q(shelf__shortname__icontains=query) |
            Q(chemical__property__property_name__icontains=query)
        )

        return object_list
