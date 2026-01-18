"""
This module handles viewing and displaying employee data.
"""
import sqlite3

conn = sqlite3.connect("ems.db")
cur = conn.cursor()
cur.execute("SELECT * FROM employees")
print(cur.fetchall())
