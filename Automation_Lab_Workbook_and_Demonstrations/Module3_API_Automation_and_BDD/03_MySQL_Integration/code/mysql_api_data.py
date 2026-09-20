import mysql.connector

# Connect to the MySQL database.
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=input("MySQL password: "),
    database="api_automation_db"
)

cursor = connection.cursor()

# Read API-style user data from MySQL.
cursor.execute(
    "SELECT id, name, email, city FROM api_users ORDER BY id"
)

rows = cursor.fetchall()

print("\nAPI User Data:")
for row in rows:
    print(row)

# Validate the retrieved data.
assert len(rows) == 3
assert rows[0][1] == "John Doe"
assert rows[1][3] == "Siliguri"

# Insert a new record using parameterized SQL.
insert_query = """
INSERT INTO api_users (id, name, email, city)
VALUES (%s, %s, %s, %s)
"""

new_user = (
    4,
    "API Test User",
    "api@test.com",
    "Mumbai"
)

cursor.execute(insert_query, new_user)
connection.commit()

print("\nInserted:", cursor.rowcount)

# Verify the inserted record.
cursor.execute(
    "SELECT id, name, email, city FROM api_users WHERE id = %s",
    (4,)
)

inserted_user = cursor.fetchone()

print("Verified:", inserted_user)

assert inserted_user[1] == "API Test User"

# Clean up the test record.
cursor.execute(
    "DELETE FROM api_users WHERE id = %s",
    (4,)
)
connection.commit()

print("Deleted test record:", cursor.rowcount)

cursor.close()
connection.close()

print("\nPASS: MySQL API data integration completed.")

