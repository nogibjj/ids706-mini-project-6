# Complex SQL Query for a MySQL Database 

![CI](https://github.com/nogibjj/ids706-mini-project-6/actions/workflows/main.yml/badge.svg)


This is a Python project that demonstrates how to create a script for executing a complex SQL query on a MySQL database. The project includes a script that connects to a MySQL database and runs a complex SQL query, which involves joins, aggregation, and sorting operations. The query retrieves specific information from the database and provides detailed insights based on the data. Additionally, the project includes tests to verify the functionality of the query.

### Explanation of the query

* ```SELECT u.name, u.age, SUM(o.total_amount) AS total_order_amount```
This part specifies what information we want to retrieve. We are selecting the name and age from the "users" table and calculating the total order amount from the "orders" table. The AS total_order_amount renames the calculated total as "total_order_amount."

* ```FROM users u```
Here, we specify that we want to retrieve data from the "users" table and give it the alias "u" to make the query more readable.

* ```LEFT JOIN orders o ON u.id = o.user_id```
This part performs a left join between the "users" table (aliased as "u") and the "orders" table (aliased as "o"). It connects rows in the "users" table with matching rows in the "orders" table based on the "id" column in "users" and the "user_id" column in "orders."

* ```GROUP BY u.id, u.name, u.age```
After joining the tables, we group the results based on the columns "id," "name," and "age" from the "users" table. This means that we'll get one row for each unique combination of these columns.

* ```ORDER BY u.age```
Finally, we order the grouped results by the "age" column in ascending order. This means the results will be sorted from the youngest to the oldest.

## Prerequisites
 
Before running this project, make sure you have the following:

* A MySQL database instance accessible from your Python environment.

## Getting Started

Follow these steps to set up and run the project:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/nogibjj/ids706-mini-project-6.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ids706-mini-project-6
   ```
   
3. Install the required Python packages by running:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables by creating a .env file in the project directory with the following content:

   ```bash
   DB_HOST='your_host'
   DB_NAME='your_db_name'
   DB_USER='your_username'
   DB_PASSWORD='your_password'
   ```

5. Create a MySQL database table by running:

   ```bash
   python main.py
   ```

6. Run the tests to ensure everything is working as expected:

   ```bash
   python test.py
   ```
