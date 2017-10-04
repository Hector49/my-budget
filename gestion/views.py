from django.shortcuts import redirect, render, get_object_or_404
from .models import Compte
from .forms import CompteForm


def compte_list(request):
    comptes = Compte.objects.order_by('numero')
    return render(request, 'gestion/compte_list.html', {'comptes':comptes})

def compte_detail(request, pk):
    compte = get_object_or_404(Compte, pk=pk)
    return render(request, 'gestion/compte_detail.html', {'compte':compte})

def compte_new(request):
    form = CompteForm(request.POST)
    if form.is_valid():
        compte = form.save(commit=False)
        compte.solde = 0.00
        compte.save()
        return redirect('compte_detail', pk=compte.pk)
    else:
        form = CompteForm()
    return render(request,'gestion/compte_edit.html', {'form':form})

def compte_edit(request, pk):
    compte = get_object_or_404(Compte, pk=pk)
    if request.method == "POST":
        form = CompteForm(request.POST, instance=compte)
        if form.is_valid():
            compte = form.save(commit=False)

            compte.save()
            return redirect('compte_detail', pk=compte.pk)
    else:
        form = CompteForm(instance=compte)
    return render(request, 'gestion/compte_edit.html', {'form': form})
