# -*- coding: utf-8 -*-

from django.contrib import admin
from gestion.models import Ecriture, Compte, Mouvement, Poste, Cause


class EcritureAdmin(admin.ModelAdmin):

    # Configuration de la liste d'articles
    list_display   = ( 'compte', 'jour', 'date', 'mouv',
    'poste', 'cause', 'debit', 'credit', 'commentaires')
    list_filter    = ('poste','cause','compte', 'mouv')
    ordering_reverse       = ('id', )

    fields = ( 'compte', 'jour', 'mouv', 'poste', 'cause', 'debit', 'credit', 'commentaires', 'validee', 'mensuelle')

class CompteAdmin(admin.ModelAdmin):

    # Configuration de la liste d'articles
    list_display   = ('numero', 'libelle', 'solde')
    list_filter    = ('numero','libelle', )
    ordering       = ('id', )

    fields = ('numero', 'libelle','solde')

class MouvementAdmin(admin.ModelAdmin):

    # Configuration de la liste d'articles
    list_display   = ('mouv', 'libelle', 'compte')
    list_filter    = ('mouv','libelle', )
    ordering       = ('id', )

    fields = ('mouv', 'libelle','compte')

class PosteAdmin(admin.ModelAdmin):

    # Configuration de la liste d'articles
    list_display   = ('nom', 'cumul', 'compte')
    list_filter    = ('nom','compte', )
    ordering       = ('id', )

    fields = ('nom', 'cumul','compte')

class CauseAdmin(admin.ModelAdmin):

    # Configuration de la liste d'articles
    list_display   = ('nom', 'cumul', 'compte')
    list_filter    = ('nom','compte', )
    ordering       = ('id', )

    fields = ('nom', 'cumul','compte')

admin.site.register(Ecriture, EcritureAdmin)
admin.site.register(Compte, CompteAdmin)
admin.site.register(Poste, PosteAdmin)
admin.site.register(Cause, CauseAdmin)
admin.site.register(Mouvement, MouvementAdmin)
