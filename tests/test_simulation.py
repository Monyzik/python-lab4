import pytest

from src.common.exceptions import NegativeArgumentException
from src.simulation import run_simulation


@pytest.mark.repeat(10)
def test_simulation(caplog):
    run_simulation()
    assert "ERROR" not in caplog.text


def test_simulation_with_many_steps(caplog):
    run_simulation(steps=1000)
    assert "ERROR" not in caplog.text


def test_simulation_seed(caplog):
    run_simulation(20, seed=-1)
    out1 = caplog.text
    caplog.clear()
    run_simulation(20, seed=-1)
    out2 = caplog.text
    assert out1 == out2


def test_negative_argument_simulation():
    with pytest.raises(NegativeArgumentException):
        run_simulation(-20)
