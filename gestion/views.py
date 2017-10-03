from django.shortcuts import redirect, render, get_object_or_404
from .models import Compte


def compte_list(request):
    comptes = Compte.objects.order_by('numero')
    return render(request, 'gestion/compte_list.html', {'comptes':comptes})

def compte_detail(request, pk):
    compte = get_object_or_404(Compte, pk=pk)
    return render(request, 'gestion/compte_detail.html', {'compte':compte})
