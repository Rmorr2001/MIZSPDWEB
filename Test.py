import psycopg2

def test_db_connection():
    try:
        conn = psycopg2.connect(
            host="spd-database.c5a06gc04xhc.us-east-1.rds.amazonaws.com",
            database="postgres",
            user="ADMIN1",
            password="Mizzou1Engineering!"
        )
        conn.close()
        return True
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        return False

if test_db_connection():
    print("Connection successful")
else:
    print("Connection failed")
