import psycopg2


def create_tables():
    connection_params = {
        'dbname': 'inventorydatabase',
        'user': 'radin',
        'password': 'Admin@4763',
        'host': 'localhost',
        'port': '5432'
    }

    try:
        conn = psycopg2.connect(**connection_params)
        cursor = conn.cursor()

        cursor.execute('''  
        CREATE TABLE IF NOT EXISTS inventory (  
            id SERIAL PRIMARY KEY,  
            name VARCHAR(255),  
            quantity INTEGER,  
            price DECIMAL,  
            type VARCHAR(50),  
            weight DECIMAL,  
            dimensions VARCHAR(255),  
            file_size DECIMAL,  
            download_link VARCHAR(255),  
            date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
        );  
        ''')

        print("Tables created successfully.")

        conn.commit()

    except Exception as e:
        print(f"An error occurred while creating tables: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()



create_tables()