import pytest
from tournoi.models import Equipe
def test_une_equipe_a_un_nom_et_une_promo(db):
    equipe = Equipe.objects.create(nom="Les Lions",promo="L1")
    
    assert equipe.nom
    assert equipe.promo


def test_deux_equipes_ne_peuvent_pas_avoir_le_meme_nom(db):
    Equipe.objects.create(nom="Les Lions", promo="L1")
        with pytest.raises(Exception):
        nouveau_nom = "Les Lions"
        
        