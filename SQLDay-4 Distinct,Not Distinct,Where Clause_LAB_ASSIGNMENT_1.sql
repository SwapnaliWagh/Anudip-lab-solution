lab30_SQL:ASSIGNMENT NO.1

mysql> CREATE DATABASE Bank;
Query OK, 1 row affected (0.01 sec)

mysql> USE Bank;
Database changed

mysql> CREATE TABLE BankAccount (account_id INT PRIMARY KEY, account_holder_name VARCHAR(100) NOT NULL, account_balance DECIMAL(15, 2)NOT NULL);
Query OK, 0 rows affected (0.03 sec)

mysql> DESC BankAccount;
+---------------------+---------------+------+-----+---------+-------+
| Field               | Type          | Null | Key | Default | Extra |
+---------------------+---------------+------+-----+---------+-------+
| account_id          | int           | NO   | PRI | NULL    |       |
| account_holder_name | varchar(100)  | NO   |     | NULL    |       |
| account_balance     | decimal(15,2) | NO   |     | NULL    |       |
+---------------------+---------------+------+-----+---------+-------+
3 rows in set (0.02 sec)

/* Task 1: Insert Data Write an SQL INSERT statement to insert data into the BankAccount table. */

mysql> INSERT INTO BankAccount (account_id, account_holder_name, account_balance) VALUES (101, 'Ismail Khan', 25000), (102, 'Sonali Thule', 32000), (103, 'Kunal Gupta', 70000), (104, 'Swapnali Wagh', 12000), (105, 'Anit Gupta', 28000), (106
, 'Janhavi Mane', 36000);

Query OK, 6 rows affected (0.01 sec)
Records: 6  Duplicates: 0  Warnings: 0

mysql> SELECT* FROM BankAccount;
+------------+---------------------+-----------------+
| account_id | account_holder_name | account_balance |
+------------+---------------------+-----------------+
|        101 | Ismail Khan         |        25000.00 |
|        102 | Sonali Thule        |        32000.00 |
|        103 | Kunal Gupta         |        70000.00 |
|        104 | Swapnali Wagh       |        12000.00 |
|        105 | Anit Gupta          |        28000.00 |
|        106 | Janhavi Mane        |        36000.00 |
+------------+---------------------+-----------------+
6 rows in set (0.00 sec)

/*Task 2: Retrieving Data Write an SQL SELECT statement to retrieve the account_holder_name and account_balance of all account holders from the BankAccount table.*/

mysql> SELECT account_holder_name, account_balance FROM BankAccount;
+---------------------+-----------------+
| account_holder_name | account_balance |
+---------------------+-----------------+
| Ismail Khan         |        25000.00 |
| Sonali Thule        |        32000.00 |
| Kunal Gupta         |        70000.00 |
| Swapnali Wagh       |        12000.00 |
| Anit Gupta          |        28000.00 |
| Janhavi Mane        |        36000.00 |
+---------------------+-----------------+
6 rows in set (0.00 sec)

/* Task 3: Filtering Data Write an SQL SELECT statement to retrieve the account_holder_name and account_balance where the account_balance is more than 30,000.*/ 


mysql> SELECT account_holder_name, account_balance FROM BankAccount WHERE account_balance > 30000;
+---------------------+-----------------+
| account_holder_name | account_balance |
+---------------------+-----------------+
| Sonali Thule        |        32000.00 |
| Kunal Gupta         |        70000.00 |
| Janhavi Mane        |        36000.00 |
+---------------------+-----------------+
3 rows in set (0.00 sec)

/*Task 4: Updating Data Write an SQL UPDATE statement to change the account_balance of the account holder whose ID is 101. */

mysql> UPDATE BankAccount SET account_balance = 30000 WHERE account_id = 101;
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT* FROM BankAccount;
+------------+---------------------+-----------------+
| account_id | account_holder_name | account_balance |
+------------+---------------------+-----------------+
|        101 | Ismail Khan         |        30000.00 |
|        102 | Sonali Thule        |        32000.00 |
|        103 | Kunal Gupta         |        70000.00 |
|        104 | Swapnali Wagh       |        12000.00 |
|        105 | Anit Gupta          |        28000.00 |
|        106 | Janhavi Mane        |        36000.00 |
+------------+---------------------+-----------------+
6 rows in set (0.00 sec)

