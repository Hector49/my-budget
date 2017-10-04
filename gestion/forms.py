from django import forms
from .models import Compte, Poste, Cause, Mouvement

class CompteForm(forms.ModelForm):
    class Meta:
        model = Compte
        fields = ('numero','libelle','solde',)

class PosteForm(forms.ModelForm):
    class Meta:
        model = Poste
        fields = ('nom','cumul','compte',)

class CauseForm(forms.ModelForm):
    class Meta:
        model = Cause
        fields = ('nom','cumul','compte',)

class MouvementForm(forms.ModelForm):
    class Meta:
        model = Mouvement
        fields = ('mouv','libelle','cumul','compte',)
