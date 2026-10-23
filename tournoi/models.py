# from django.db import models  # noqa: F401
# from django.core.exceptions import ValidationError   

# # Register your models here.


# class Equipe(models.Model):
#     """Model definition for MODELNAME."""

#     PROMO = [("l1", "L1"), ("l2", "L2"),("l3", "L3")]

#     # TODO: Define fields here
#     nom = models.CharField(max_length=100,unique=True)
#     promo = models.CharField(max_length=5,choices=PROMO)

#     class Meta:

#         verbose_name = "Equipe"
#         verbose_name_plural = "Equipes"

#     def __str__(self):
#         return f"{self.nom}"




# class Match(models.Model):
#     date = models.DateField()
#     equipe_visiteur = models.ForeignKey(Equipe,on_delete=models.SET_NULL)
#     equipe_domicile = models.ForeignKey(Equipe,on_delete=models.SET_NULL)
#     score_domicile = models.IntegerField(null=True,blank=True)
#     score_visiteur = models.IntegerField(null=True,blank=True)
#     joue = models.BooleanField(default=False)
    
    
#     def clean(self):
#         if self.joue and (self.score_a is None or self.score_b is None):
#             raise ValidationError("Score requis pour un match joué.")
#         if not self.joue and (self.score_a is not None or self.score_b is not None):
#             raise ValidationError("Score interdit pour un match non joué.")   
    
    
#     def __str__(self):
#         return f"Les {self.equipe_domicile}: {self.score_equipe_domicile}-{self.score_equipe_domicile}"


from django.core.exceptions import ValidationError
from django.db import models


class Equipe(models.Model):
    PROMO = [("L1", "L1"), ("L2", "L2"), ("L3", "L3")]

    nom = models.CharField(max_length=100, unique=True)
    promo = models.CharField(max_length=5, choices=PROMO)

    def __str__(self):
        return self.nom


class Match(models.Model):
    date = models.DateField()
    equipe_visiteur = models.ForeignKey(
        Equipe,
        on_delete=models.CASCADE,
        related_name="matchs_a_l_exterieur",
    )
    equipe_domicile = models.ForeignKey(
        Equipe,
        on_delete=models.CASCADE,
        related_name="matchs_a_domicile",
    )
    score_domicile = models.IntegerField(null=True, blank=True)
    score_visiteur = models.IntegerField(null=True, blank=True)
    joue = models.BooleanField(default=False)

    def clean(self):
        if self.joue and (
            self.score_domicile is None or self.score_visiteur is None
        ):
            raise ValidationError("Score requis pour un match joué.")

        if not self.joue and (
            self.score_domicile is not None or self.score_visiteur is not None
        ):
            raise ValidationError("Score interdit pour un match non joué.")

    def __str__(self):
        return (
            f"{self.equipe_domicile} – {self.equipe_visiteur} "
            f"({self.score_domicile}-{self.score_visiteur})"
        )
