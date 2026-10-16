from tournoi.models import Equipe
def test_une_equipe_a_un_nom_et_une_promo(db):
    equipe = Equipe.objects.create(nom="Les Lions",promo="L1")
    nom_existe = Equipe.objects.filter(nom=nouveau_nom).exists()
    
    assert not nom_existe, f"L'équipe '{nouveau_nom}' existe déjà !"
    
    assert equipe.nom
    assert equipe.promo



