import pytest
from tournoi.models import Equipe





def test_une_equipe_a_un_nom_et_une_promo(db):
    equipe = Equipe.objects.create(nom="Les Lions",promo="L1")
    
    assert equipe.nom
    assert equipe.promo


def test_deux_equipes_ne_peuvent_pas_avoir_le_meme_nom(db):

    Equipe.objects.create(nom="Les Lions", promo="L1")
    with pytest.raises(Exception):
        Equipe.objects.create(nom="Les Lions", promo="L1")

        

   

def test_une_equipe_s_affiche_par_son_nom(db):
    equipe = Equipe.objects.create(nom="Les Lions", promo="L1")
    
    assert str(equipe) == "Les Lions"



def test_un_match_oppose_deux_equipes(db):
    domicile = Equipe.objects.create(nom="Les Lions", promo="L1")
    exterieur = Equipe.objects.create(nom="Les Éperviers", promo="L1")
    
    match = Match.objects.create(equipe_domicile=domicile, equipe_visiteuse=exterieur)
    
    assert match.equipe_domicile == domicile
    assert match.equipe_visiteuse == exterieur


def test_tant_qu_un_match_n_est_pas_joue_le_score_est_inconnu(db):
    domicile = Equipe.objects.create(nom="Les Lions", promo="L1")
    exterieur = Equipe.objects.create(nom="Les Éperviers", promo="L1")
    match = Match.objects.create(equipe_domicile=domicile, equipe_visiteuse=exterieur)
    
    assert match.score_domicile is None
    assert match.score_visiteur is None




        