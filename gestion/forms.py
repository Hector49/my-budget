from django import forms
from .models import Compte, Poste, Cause, Mouvement,Ecriture

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

class EcritureForm(forms.ModelForm):
    class Meta:
        model = Ecriture
        fields = ('compte', 'jour', 'mouv', 'poste', 'cause', 'debit', 'credit', 'commentaires', 'validee', 'mensuelle')
