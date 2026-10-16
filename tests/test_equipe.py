from tournoi.models import Equipe
def test_une_equipe_a_un_nom_et_une_promo(db):
    equipe = Equipe.objects.create(nom="Les Lions",promo="L1")
   
    assert equipe.nom=="Les Lions"
    assert equipe.promo in["L1","L2","L3"]


