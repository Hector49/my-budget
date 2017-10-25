from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Compte, Poste, Cause, Mouvement, Ecriture
from .forms import CompteForm, PosteForm, CauseForm, MouvementForm, EcritureForm



class ListeView(generic.ListView):
    template_name = 'gestion/listecompte.html'
    context_object_name = 'latest_compte_list'
    paginate_by = 4

    def get_queryset(self):
        """Return the last five published questions."""
        return Compte.objects.order_by('numero')

class DetailCompteView(generic.DetailView):
    context_object_name='compte'
    model = Compte
    template_name = 'gestion/detailcompte.html'

    def get_context_data(self, **kwargs):
        context = super(DetailCompteView, self).get_context_data(**kwargs)
        context['ecriture_list'] = 'mes ecritures'
        return context


#ECRITURE
class IndexView(generic.ListView):
    template_name = 'gestion/index.html'
    context_object_name = 'latest_ecriture_list'
    paginate_by = 15

    def get_queryset(self):
        """Return the last five published questions."""
        return Ecriture.objects.filter(compte__id=self.kwargs['id']).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['ecriture'] = 'mon ecriture'
        return context


class DetailView(generic.DetailView):
    model = Ecriture
    template_name = 'gestion/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['commentaires'] = 'mon operation'
        return context


class CreateView(generic.CreateView):
    model = Ecriture
    fields = [ 'compte', 'jour', 'mouv', 'poste', 'cause', 'debit', 'credit', 'commentaires', 'validee', 'mensuelle']
    template_name = 'gestion/edit.html'

    def get_success_url(self):
        return reverse('gestion:listecompte')

class UpdateView(generic.UpdateView):
    model = Ecriture
    template_name = 'gestion/edit.html'
    form_class = EcritureForm

    def get_success_url(self):
        return reverse('gestion:listecompte')

#Compte
def compte_list(request):
    comptes = Compte.objects.order_by('numero')
    paginator = Paginator(comptes, 3) # Show 3 comptess per page

    page = request.GET.get('page')
    try:
        comptes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        comptes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        comptes = paginator.page(paginator.num_pages)
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
        return redirect('gestion:compte_detail', pk=compte.pk)
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
            return redirect('gestion:compte_detail', pk=compte.pk)
    else:
        form = CompteForm(instance=compte)
    return render(request, 'gestion/compte_edit.html', {'form': form})

#POSTE
def poste_list(request):
    postes = Poste.objects.order_by('nom')
    paginator = Paginator(postes, 6) # Show 6 contacts per page

    page = request.GET.get('page')
    try:
        postes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        postes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        postes = paginator.page(paginator.num_pages)

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
        return redirect('gestion:poste_detail', pk=poste.pk)
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
            return redirect('gestion:poste_detail', pk=poste.pk)
    else:
        form = PosteForm(instance=poste)
    return render(request, 'gestion/poste_edit.html', {'form': form})

#CAUSE
def cause_list(request):
    causes = Cause.objects.order_by('nom')
    paginator = Paginator(causes, 10) # Show 10 causes per page

    page = request.GET.get('page')
    try:
        causes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        causes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        causes = paginator.page(paginator.num_pages)
    return render(request, 'gestion/cause_list.html', {'causes':causes})

def cause_detail(request, pk):
    cause = get_object_or_404(Cause, pk=pk)
    return render(request, 'gestion/cause_detail.html', {'cause':cause})

def cause_new(request):
    form = CauseForm(request.POST)
    if form.is_valid():
        cause = form.save(commit=False)
        cause.save()
        return redirect('gestion:cause_detail', pk=cause.pk)
    else:
        form = CauseForm()
    return render(request,'gestion/cause_edit.html', {'form':form})

def cause_edit(request, pk):
    cause = get_object_or_404(Cause, pk=pk)
    if request.method == "POST":
        form = CauseForm(request.POST, instance=cause)
        if form.is_valid():
            cause = form.save(commit=False)
            cause.save()
            return redirect('gestion:cause_detail', pk=cause.pk)
    else:
        form = CauseForm(instance=cause)
    return render(request, 'gestion/cause_edit.html', {'form': form})

#MOUVEMENT
def mouvement_list(request):
    mouvements = Mouvement.objects.order_by('libelle')
    return render(request, 'gestion/mouvement_list.html', {'mouvements':mouvements})

def mouvement_detail(request, pk):
    mouvement = get_object_or_404(Mouvement, pk=pk)
    return render(request, 'gestion/mouvement_detail.html', {'mouvement':mouvement})

def mouvement_new(request):
    form = MouvementForm(request.POST)
    if form.is_valid():
        mouvement = form.save(commit=False)
        mouvement.cumul = 0.00
        mouvement.save()
        return redirect('gestion:mouvement_detail', pk=mouvement.pk)
    else:
        form = MouvementForm()
    return render(request,'gestion/mouvement_edit.html', {'form':form})

def mouvement_edit(request, pk):
    mouvement = get_object_or_404(Mouvement, pk=pk)
    if request.method == "POST":
        form = MouvementForm(request.POST, instance=mouvement)
        if form.is_valid():
            mouvement = form.save(commit=False)
            mouvement.save()
            return redirect('gestion:mouvement_detail', pk=mouvement.pk)
    else:
        form = MouvementForm(instance=mouvement)
    return render(request, 'gestion/mouvement_edit.html', {'form': form})
