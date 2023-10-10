# Complex SQL Query for a MySQL Database 

![CI](https://github.com/aghakishiyeva/ids706-mini-project-6/actions/workflows/main.yml/badge.svg)


This is a Python project that demonstrates how to create a script for executing a complex SQL query on a MySQL database. The project includes a script that connects to a MySQL database and runs a complex SQL query, which involves joins, aggregation, and sorting operations. The query retrieves specific information from the database and provides detailed insights based on the data. Additionally, the project includes tests to verify the functionality of the query.


## Prerequisites

Before running this project, make sure you have the following:

* A MySQL database instance accessible from your Python environment.

## Getting Started

Follow these steps to set up and run the project:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/aghakishiyeva/ids706-mini-project-6.git
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
