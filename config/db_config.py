DB_CONFIG = {
'host': 'localhost',
'port': 5432,
'database': 'stock_market_db',
'user': 'postgres',
'password': ''
}

DATABASE_URL = f"postgresql://{DB_CONFIG['user']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
SQLALCHEMY_DATABASE_URL = DATABASE_URL

TEST_SETTINGS = {
'verbose': True,
'timeout': 5
}
