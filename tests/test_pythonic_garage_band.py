from pythonic_garage_band import __version__
from pythonic_garage_band.pythonic_garage_band import Band,Muscians,Guitarest,Drummer,Singer,Bassist
import pytest
def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def prep_data():
    bashar =Guitarest("Bashar")
    samer = Bassist("Samer")
    saed = Drummer("Saed")
    ahmad = Singer("Ahmad")
    band1 = (Band("Pandora Box", [ahmad,bashar, samer, saed]))
    return {'bashar':bashar,'samer':samer,'saed':saed,'ahmad':ahmad}
def test_repr(prep_data):
    expected = 'Bassist:Samer'
    actual = prep_data['samer'].__repr__()
    assert actual == expected
def test_str(prep_data):
    expected='Am Bashar, i play Guitar'
    actual = prep_data['bashar'].__str__()
    assert expected == actual
def test_get_instrument(prep_data):
    acutal = prep_data['saed'].get_instrument()
    expected = 'Drums'
    assert expected==acutal

def test_play_solo(prep_data):
    actual = prep_data['ahmad'].play_solo()
    expected = 'AAAAAAAAAAAHHHHHHHHHHHHH'
    assert expected ==actual
