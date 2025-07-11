import pymysql

class Person:
    def __init__(self, name="", gender="", dob="", location=""):
        self.name = name
        self.gender = gender
        self.dob = dob
        self.location = location

    def __str__(self):
        return f'Name: {self.name}, Location: {self.location}'

class Db_operations:
    def __init__(self):
        self.connection = None

    def connect_db(self):
        """Establishes a connection to the database."""
        try:
            self.connection = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                password='findaditya1125',
                database='aditya11_db',
                charset='utf8'
            )
            print('DB connected')
        except pymysql.MySQLError as e:
            print(f'DB connection failed: {e}')
            self.connection = None
            raise

    def disconnect_db(self):
        """Closes the database connection."""
        if self.connection:
            try:
                self.connection.close()
                print('DB disconnected')
            except pymysql.MySQLError as e:
                print(f'Error while disconnecting DB: {e}')

    def create_db(self):
        """Creates the database if it doesn't exist."""
        self.connect_db()
        if self.connection:
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute('CREATE DATABASE IF NOT EXISTS aditya11_db;')
                    print('DB created')
                self.connection.commit()
            except pymysql.MySQLError as e:
                print(f'Error creating DB: {e}')
            finally:
                self.disconnect_db()

    def create_table(self):
        """Creates the 'person' table if it doesn't exist."""
        self.connect_db()
        if self.connection:
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS person (
                            id INT PRIMARY KEY AUTO_INCREMENT,
                            name VARCHAR(32) NOT NULL,
                            gender CHAR(1) CHECK(gender IN ('m', 'M', 'f', 'F')),
                            location VARCHAR(32),
                            dob DATE
                        );
                    """)
                    print('Table created')
                self.connection.commit()
            except pymysql.MySQLError as e:
                print(f'Error creating table: {e}')
            finally:
                self.disconnect_db()

    def get_latest_row_id(self):
        """Fetches the ID of the last inserted person."""
        if self.connection:
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute('SELECT MAX(id) FROM person;')
                    result = cursor.fetchone()
                    return result[0] if result else None
            except pymysql.MySQLError as e:
                print(f'Error fetching latest row ID: {e}')
                return None
        else:
            print('No active database connection.')
            return None
