import source.shapes as shapes
import pytest


def area_check(my_rectangle):
    assert my_rectangle.area() == 10 * 20

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 10*2 + 20*2

def test_equality(my_rectangle, another_same_rectangle):
    assert my_rectangle == another_same_rectangle

def test_inequality(my_rectangle, another_different_rectangle):
    assert my_rectangle != another_different_rectangle