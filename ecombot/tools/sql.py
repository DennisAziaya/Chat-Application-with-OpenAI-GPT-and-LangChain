import sqlite3

from langchain_core.tools import Tool

conn = sqlite3.connect("db.sqlite")


def run_sql_query(sql_query):
    cursor = conn.cursor()
    cursor.execute(sql_query)
    return cursor.fetchall()


run_query_tool = Tool.from_fuction(
    name="execute_a_query",
    description="Execute a sqlite query",
    func=run_sql_query,
)
