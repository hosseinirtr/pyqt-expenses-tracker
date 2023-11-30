import pytest
from project import add_user, add_transaction, get_transactions, get_expenses, get_income, remove_user

def setup_function(function):
    # Add a user for testing
    remove_user('TestUser')
    user_id, _ = add_user('TestUser')
    return user_id

def test_add_transaction():
    # Add a transaction and check if it was added correctly
    user_id = setup_function(add_user)
    add_transaction(user_id, 100.0, True,'Test Transaction',)
    transactions = get_transactions(user_id)
    assert len(transactions) == 1
    assert transactions[0].amount == 100.0
    assert transactions[0].is_income == True

def test_get_expenses():
    # Add an expense and check if it's returned by get_expenses
    user_id = setup_function(add_user)
    add_transaction(user_id, 50.0, False, 'Test Expense')
    expenses = get_expenses(user_id)
    assert len(expenses) == 1
    assert expenses[0].amount == 50.0

def test_get_income():
    # Add an income and check if it's returned by get_income
    user_id = setup_function(add_user)
    add_transaction(user_id, 200.0, True, 'Test Income')
    incomes = get_income(user_id)
    assert len(incomes) == 1
    assert incomes[0].amount == 200.0