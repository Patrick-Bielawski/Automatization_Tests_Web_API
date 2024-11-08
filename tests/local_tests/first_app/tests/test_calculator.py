import pytest # Importování balíčků pytest
from src import calculator # importování testovací kalkulačky


def test_add():
    assert calculator.add(6, 5) == 11

def test_substrack():
    assert calculator.substract(10, 5) == 5

def test_add_wrong():
    assert calculator.add_wrong(0, 0) == 0  # testovat více vstupů 

def test_multiply():
    assert calculator.multiply(10, 10) == 100

def test_multiply_wrong():
    assert calculator.multiply_wrong(2, 2) == 4



# Spouštění testů
# 
# pytest -v , pytest -s , pytest -v --tb=long , pytest -m slow , pytest --junitxml=path/to/report.xml