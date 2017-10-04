from django.shortcuts import redirect, render, get_object_or_404
from .models import Compte, Poste
from .forms import CompteForm, PosteForm


#Compte
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

#POSTE
def poste_list(request):
    postes = Poste.objects.order_by('nom')
    return render(request, 'gestion/poste_list.html', {'postes':postes})

def poste_detail(request, pk):
    poste = get_object_or_404(Poste, pk=pk)
    return render(request, 'gestion/poste_detail.html', {'poste':poste})

def poste_new(request):
    form = PosteForm(request.POST)
    if form.is_valid():
        poste = form.save(commit=False)
        poste.cumul = 0.00
        poste.save()
        return redirect('poste_detail', pk=poste.pk)
    else:
        form = PosteForm()
    return render(request,'gestion/poste_edit.html', {'form':form})

def poste_edit(request, pk):
    poste = get_object_or_404(Poste, pk=pk)
    if request.method == "POST":
        form = PosteForm(request.POST, instance=poste)
        if form.is_valid():
            poste = form.save(commit=False)
            poste.save()
            return redirect('poste_detail', pk=poste.pk)
    else:
        form = PosteForm(instance=poste)
    return render(request, 'gestion/poste_edit.html', {'form': form})
