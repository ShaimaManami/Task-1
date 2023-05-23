
import json
import pymysql

# Connect to the MySQL database
connection = pymysql.connect(
host="localhost",
user="root",
password="Shaima24$",
database="task_schema",
port=3306
)

# Create a cursor
cursor = connection.cursor()

# Insert the JSON data into the Cities table
for city in json.load(open("others/cities.json")):
    cursor.execute("""
INSERT INTO cities (
city_id,
region_id,
name_ar,
name_en,
longitude,
latitude
) VALUES (
%s,
%s,
%s,
%s,
%s,
%s
)
""", (
city["city_id"],
city["region_id"],
city["name_ar"],
city["name_en"],
city["center"][0],
city["center"][1]
))

# Commit the changes to the database
connection.commit()

# Close the connection to the database
connection.close()