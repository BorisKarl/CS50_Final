
"""
    class Orders(db.Model):
    __tablename__ = 'orders'
    __table_args__ = {'extend_existing': True}
    LOC_CODE = db.Column(db.Text, primary_key=True)

        con = sqlite3.connect("namo.db")
        cur = con.cursor()
        con.commit()
        con.close()


        ("INSERT INTO orders (item_id, price, shipping, total, number) VALUES(?,?,?,?,?)",
                    [item_id, price, shipping, total, number])
        
        
        query = "INSERT INTO users (name, email) VALUES (?, ?)"

    # Define variables with the data to be inserted
    name = 'Alice'
    email = 'alice@example.com'

    # Execute the SQL query with the variables as parameters
    cursor.execute(query, (name, email))

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

        data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit()
        """


"""








"""


engine = create_engine("sqlite:///namo.db")

try:
    connection = engine.connect()
    print("Success")
except Exception as e:
    print("Fail", e)
