LAB31:SQL:Day-7(Qualifiers,Having Caluse,Alter Table,Transactions) 


mysql> use anpc8905;
Database changed

/*Task1: Create a table Person with PersonID int, FirstName varchar(255), LastName varchar(255) and age (int). Make PersonID PRIMARY KEY. */

mysql> CREATE TABLE Person (PersonID INT PRIMARY KEY, FirstName VARCHAR(255), LastName VARCHAR(255), age INT);
Query OK, 0 rows affected (0.06 sec)

/* Task 3: Insert data to Person table*/
mysql> INSERT INTO Person (PersonID, FirstName, LastName, age) VALUES (1, 'Sonali', 'Thule', 24), (2, 'Kunal', 'Gupta', 23), (3, 'Janhavi', 'Mane', 25), (4, 'Ismail', 'Khan', 22), (6, 'Sneha', 'Shukla', 21);
Query OK, 5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> select*from Person;
+----------+-----------+----------+------+
| PersonID | FirstName | LastName | age  |
+----------+-----------+----------+------+
|        1 | Sonali    | Thule    |   24 |
|        2 | Kunal     | Gupta    |   23 |
|        3 | Janhavi   | Mane     |   25 |
|        4 | Ismail    | Khan     |   22 |
|        5 | Sneha     | Shukla   |   21 |
+----------+-----------+----------+------+
5 rows in set (0.00 sec)

/*Task2: Create a table Employee with emp_id int, first_name varchar(255), last_name varchar(255) and age (int ) Make emp_id PRIMARY KEY.*/

mysql> CREATE TABLE Employee (emp_id INT PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255), age INT);
Query OK, 0 rows affected (0.02 sec)

/* Task 4: Insert data to Employee table */

mysql> INSERT INTO Employee (emp_id, first_name, last_name, age) VALUES (101, 'Kunal', 'Gupta', 23), (102, 'Sonali', 'Thule', 24), (103, 'Fairaaz', 'Ahmed', 23), (104, 'Akansha', 'Kotian', 22), (105, 'Rutuja', 'Vilankar', 24);
Query OK, 5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> select*from Employee;
+--------+------------+-----------+------+
| emp_id | first_name | last_name | age  |
+--------+------------+-----------+------+
|    101 | Kunal      | Gupta     |   23 |
|    102 | Sonali     | Thule     |   24 |
|    103 | Fairaaz    | Ahmed     |   23 |
|    104 | Akansha    | Kotian    |   22 |
|    105 | Rutuja     | Vilankar  |   24 |
+--------+------------+-----------+------+
5 rows in set (0.00 sec)

/*Task 5: Create Union of two tables */

mysql> SELECT PersonID AS ID, FirstName AS First_Name, LastName AS Last_Name, Age FROM Person UNION SELECT emp_id AS ID, first_name AS First_Name, last_name AS Last_Name, age FROM Employee;
+-----+------------+-----------+-----+
| ID  | First_Name | Last_Name | Age |
+-----+------------+-----------+-----+
|   1 | Sonali     | Thule     |  24 |
|   2 | Kunal      | Gupta     |  23 |
|   3 | Janhavi    | Mane      |  25 |
|   4 | Ismail     | Khan      |  22 |
|   5 | Sneha      | Shukla    |  21 |
| 101 | Kunal      | Gupta     |  23 |
| 102 | Sonali     | Thule     |  24 |
| 103 | Fairaaz    | Ahmed     |  23 |
| 104 | Akansha    | Kotian    |  22 |
| 105 | Rutuja     | Vilankar  |  24 |
+-----+------------+-----------+-----+
10 rows in set (0.00 sec)