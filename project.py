from prettytable import PrettyTable
from sqlalchemy import create_engine, Column, Integer, String, Sequence, Float, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
import sys

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50), unique=True)


class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, Sequence('transaction_id_seq'), primary_key=True)
    user_id = Column(Integer)
    amount = Column(Float)
    is_income = Column(Boolean)
    title = Column(String(50), nullable=True)


try:
    engine = create_engine('postgresql://postgres:1111@localhost:5432/expense_tracking')
    Base.metadata.create_all(engine)
except Exception as e:
    if not database_exists(engine.url):
        create_database(engine.url)
        print("Database created successfully.")
    print(f"\n\n Error:{e} \n")

    
Session = sessionmaker(bind=engine)
session = Session()


def remove_user(username):
    user = session.query(User).filter_by(username=username).first()
    print(user)
    
    if user:
        session.delete(user)
        session.commit()
        return "User deleted successfully."
    else:
        return "User does not exist."
    
def add_user(username):
    user = session.query(User).filter_by(username=username).first()
    if user:
        return [user.id, "User already exists."]
    else:
        user = User(username=username)
        session.add(user)
        session.commit()
        return [user.id, "User created successfully."]
    
    
def add_transaction(user_id, amount, is_income, title):
    transaction = Transaction(user_id=user_id, amount=amount, is_income=is_income, title=title)
    session.add(transaction)
    session.commit()

def get_transactions(user_id):
    return session.query(Transaction).filter_by(user_id=user_id).all()

def get_expenses(user_id):
    return session.query(Transaction).filter_by(user_id=user_id, is_income=False).all()

def get_income(user_id):
    return session.query(Transaction).filter_by(user_id=user_id, is_income=True).all()


def main():
    username = input("Enter username: ")
    
    if username == '':
        print("Exiting...")
        sys.exit()
    else:
        add_user(username)
        
    user = add_user(username)
    print(f'your user id is : {user[0]}')
    print(f'Status : {user[1]}')
    
    while True:
        # print help to choose command 
        print("\nCommands: add, get, get_expenses, get_income, delete_user, exit\n")
        
        command = input("Enter command: ")
        if command == 'exit':
            break;
        elif command == 'add':
            amount = input("Enter amount: ")
            is_income = input("Is income? (y/n): ")
            title = input("Enter title: ")
            if is_income == 'y':
                is_income = True
            else:
                is_income = False
            add_transaction(user[0], amount, is_income, title)
            print("\nDone \n")
        elif command == 'get':
            transactions = get_transactions(user[0])
            # find username with id
            user = session.query(User).filter_by(id=user[0]).first() # I know username is exit as variable but I want to test it 
            table = PrettyTable(['User name', 'Amount', 'Is Income', 'Title'])
            for transaction in transactions:
                table.add_row([user.username, transaction.amount, transaction.is_income, transaction.title])
            print(table)
        elif command == 'get_expenses':
            expenses = get_expenses(user[0])
            for expense in expenses:
                print(f"Expense ID: {expense.id}, Amount: {expense.amount}, Title: {expense.title}")
        elif command == 'get_income':
            incomes = get_income(user[0])
            for income in incomes:
                print(f"Income ID: {income.id}, Amount: {income.amount}, Title: {income.title}")
        elif command == 'delete_user':
            remove_user(username)
            print("User deleted successfully.")
            break;
        else:
            print("Wrong command")

if __name__ == "__main__":
    main()