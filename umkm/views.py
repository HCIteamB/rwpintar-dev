from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from .models import Umkm

def index(request):
    title_contains_query = request.GET.get('title_search')
    template = "umkm.html"
    list_alls = Umkm.objects.order_by('title')
    qs = Umkm.objects.all()
    paginator = Paginator(list_alls, 2)
    page = request.GET.get('page')
    paged_lists = paginator.get_page(page)

    if title_contains_query != '' and title_contains_query is not None:
        qs = qs.filter(title__icontains=title_contains_query)

    context = {
            'list_alls' : paged_lists,
            'queryset' : qs 
            }

    return render(request, template , context)


def umkm_views(request, list_all_id):
    list_all = get_object_or_404(Umkm, pk=list_all_id)

    context = {
            'list_all': list_all
            }

    return render(request, "umkm-detail.html", context)
