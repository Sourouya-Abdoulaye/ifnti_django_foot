from django.db import models  # noqa: F401

# Register your models here.


class Equipe(models.Model):
    """Model definition for MODELNAME."""

    PROMO = [("l1", "L1"), ("l2", "L2"),("l3", "L3")]

    # TODO: Define fields here
    nom = models.CharField(max_length=100,unique=True)
    promo = models.CharField(max_length=5,choices=PROMO)

    class Meta:

        verbose_name = "Equipe"
        verbose_name_plural = "Equipes"

    def __str__(self):
        return f"{self.nom}"




class Match(models.Model):
    date = models.DateField()
    equipe_visiteur = models.ForeignKey(Equipe,on_delete=models.SET_NULL)
    equipe_domicile = models.ForeignKey(Equipe,on_delete=models.SET_NULL)
    score_domicile = models.IntegerField(null=True,blank=True)
    score_visiteur = models.IntegerField(null=True,blank=True)
    
    
    
    def __str__(self):
        return f"Les {self.equipe_domicile}: {self.score_equipe_domicile}-{self.score_equipe_domicile}"