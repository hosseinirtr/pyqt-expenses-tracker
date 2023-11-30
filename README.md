# Expense Tracking System

#### Video Demo:  https://youtu.be/jJTwIksMKMg

#### Description:
This project is an Expense Tracking System designed to help users manage their personal finances. It allows users to add transactions, both income and expenses, and retrieve them in a tabular format for easy viewing and tracking. 
The system is built with Python and uses a PostgreSQL database to store the transactions, ensuring data persistence. It employs SQLAlchemy, a Python SQL toolkit and Object-Relational Mapping (ORM) system, for efficient and high-level database operations. 
The application is console-based, providing a simple and straightforward user interface. Users can add a transaction with details like amount, income or expense type, and a title. They can also view all their transactions, or filter them based on income or expenses. 
The system also provides the functionality to delete a user, removing all their associated transactions from the database. This project is an excellent tool for anyone looking to keep a close eye on their income and expenses.
The PostgreSQL database ensures that all transaction data is stored securely and can be retrieved quickly, even with a large number of transactions. The use of SQLAlchemy allows for complex queries to be written in a simple and Pythonic way, improving the readability and maintainability of the code.
The console-based interface ensures that the application is easy to use, even for those not familiar with more complex user interfaces. The commands are intuitive and the output is displayed in a clear and easy-to-understand format.
Overall, this Expense Tracking System is a comprehensive tool for personal finance management, providing all the necessary features in a simple and user-friendly package.
###### Libraries Used

- **SQLAlchemy**: A SQL toolkit and Object-Relational Mapping (ORM) system for Python. It's used for creating and managing the database for this application.
- **PrettyTable**: A simple Python library designed to make it quick and easy to represent tabular data in visually appealing ASCII tables.

###### Database Structure

The application uses two tables: `users` and `transactions`.

- **Users**: Stores user data. Each user has a unique `id` and `username`.
- **Transactions**: Stores transaction data. Each transaction has a unique `id`, `user_id` (referring to the user who made the transaction), `amount`, `is_income` (a boolean indicating whether the transaction is an income or an expense), and `title`.

###### Functions

- **remove_user(username)**: Deletes a user from the `users` table.
- **add_user(username)**: Adds a new user to the `users` table.
- **add_transaction(user_id, amount, is_income, title)**: Adds a new transaction to the `transactions` table.
- **get_transactions(user_id)**: Retrieves all transactions made by a specific user.
- **get_expenses(user_id)**: Retrieves all expenses (where `is_income` is False) of a specific user.
- **get_income(user_id)**: Retrieves all income (where `is_income` is True) of a specific user.


## Installation

1. Clone the repository:
    ```bash
    git clone https://submit.cs50.io/users/hosseinirtr/cs50/problems/2022/python/project
    ```

2. Navigate to the project directory:
    ```bash
    cd project
    ```

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the main script:
    ```bash
    python main.py
    ```

2. Follow the prompts to add transactions and retrieve them.

## Testing

Tests are written using pytest. To run the tests, use the following command:

```bash
pytest test_main.py