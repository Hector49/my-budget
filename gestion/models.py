from django.db import models
from django.utils import timezone


class Ecriture(models.Model):
    compte = models.ForeignKey('Compte')
    jour = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Date d'entrée")
    mouv = models.ForeignKey('Mouvement')
    poste = models.ForeignKey('Poste')
    cause = models.ForeignKey('Cause')
    debit = models.DecimalField(max_digits=10,decimal_places=2)
    credit = models.DecimalField(max_digits=10,decimal_places=2)
    commentaires = models.TextField(null=True)
    validee = models.CharField(max_length=1)
    mensuelle = models.CharField(max_length=1)
    
    def __str__(self):
        return self.commentaires

class Compte(models.Model):
    numero = models.CharField(max_length=25)
    libelle = models.TextField(null=False)
    solde = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.numero

class Cause(models.Model):
    nom = models.CharField(max_length=50)
    cumul = models.DecimalField(max_digits=10,decimal_places=2)
    compte = models.ForeignKey('Compte')

    def __str__(self):
        return self.nom

class Poste(models.Model):
    nom = models.CharField(max_length=50)
    cumul = models.DecimalField(max_digits=10,decimal_places=2)
    compte = models.ForeignKey('Compte')

    def __str__(self):
        return self.nom

class Mouvement(models.Model):
    mouv = models.CharField(max_length=2)
    libelle = models.CharField(max_length=25)
    cumul = models.DecimalField(max_digits=10,decimal_places=2)
    compte = models.ForeignKey('Compte')

    def __str__(self):
        return self.mouv
