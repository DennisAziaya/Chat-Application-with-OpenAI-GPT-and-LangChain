# Import the SQLite library
import sqlite3

# Import the Tool class from langchain_core.tools
from langchain_core.tools import Tool

# Establish a connection to the SQLite database (assuming "db.sqlite" file exists)
conn = sqlite3.connect("db.sqlite")

# Define a function to run an SQL query using the established connection
def run_sql_query(sql_query):
    # Create a cursor to execute the SQL query
    cursor = conn.cursor()
    cursor.execute(sql_query)

    # Return the results of the query
    return cursor.fetchall()

# Create a Tool instance named 'run_query_tool' using Tool.from_function
run_query_tool = Tool.from_function(
    name="execute_a_query",
    description="Execute a SQLite query",
    func=run_sql_query,
)
