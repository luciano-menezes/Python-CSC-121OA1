import pytest
from employee import Employee

# Test functions without using a fixture
def test_give_default_raise():
    emp = Employee("Lucky", "Luciano", 50000)
    emp.give_raise()
    assert emp.annual_salary == 55000

def test_give_custom_raise():
    emp = Employee("Jess", "Menezes", 60000)
    emp.give_raise(10000)
    assert emp.annual_salary == 70000
