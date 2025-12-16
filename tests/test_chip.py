import pytest

from src.objects.chip import Chip


def test_chip():
    chip = Chip(10)
    assert chip.__repr__() == "Chip(count=10)"
    assert chip.__str__() == "10"
    assert chip < 100
    assert chip == 10
    assert chip < Chip(100)
    assert chip <= Chip(10)
    assert chip == Chip(10)
    chip += 10
    assert chip.count == 20
    chip -= 10
    assert chip.count == 10
    chip += Chip(10)
    assert chip.count == 20
    chip -= Chip(10)
    assert chip.count == 10


def test_chip_type_error():
    chip = Chip(10)
    with pytest.raises(TypeError):
        print(chip <= "10")
    with pytest.raises(TypeError):
        print(chip == "10")
    with pytest.raises(TypeError):
        print(chip < "10")
    with pytest.raises(TypeError):
        chip += "10"
    with pytest.raises(TypeError):
        chip -= "10"
