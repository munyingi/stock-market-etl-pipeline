import psycopg2
from config.db_config import DB_CONFIG

def test_database_connection():
print("=" * 50)
print("Testing Database Connection...")
print("=" * 50)

try:
print(f"\n📍 Connecting to: {DB_CONFIG['host']}:{DB_CONFIG['port']}")

connection = psycopg2.connect(
host=DB_CONFIG['host'],
port=DB_CONFIG['port'],
database=DB_CONFIG['database'],
user=DB_CONFIG['user'],
password=DB_CONFIG['password']
)

cursor = connection.cursor()
cursor.execute("SELECT version();")
db_version = cursor.fetchone()

print("\n✅ CONNECTION SUCCESSFUL!\n")
print(f"PostgreSQL Version: {db_version[0]}\n")

cursor.execute("""
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
""")

tables = cursor.fetchall()
print(f"📊 Tables in database: {len(tables)}")
for table in tables:
print(f" - {table[0]}")

print("\n" + "=" * 50)
print("✅ Database ready for Part 2!")
print("=" * 50 + "\n")

cursor.close()
connection.close()
return True

except psycopg2.Error as error:
print(f"\n❌ CONNECTION FAILED!")
print(f"Error: {error}\n")
return False

if __name__ == "__main__":
test_database_connection()
