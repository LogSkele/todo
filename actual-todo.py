import sqlite3 
connection = sqlite3.connect('database.db')
cur = connection.cursor()
#cur.execute("DROP TABLE aaron;")
cur.execute("""
  CREATE TABLE Todo (
    Task TEXT NOT NULL PRIMARY KEY,
    Status TEXT
);
""")
while True:
  cur.execute("""
    SELECT COUNT(DISTINCT Task)
    FROM Todo;
  """)
  cur.execute("SELECT * FROM Todo;")
  print(cur.fetchall())
  connection.commit()
  c=input("1. create 2. delete 3. complete\n")
  if c == "1":
    tdn=input("todo name? ")
    try:
      cur.execute(f"""
        INSERT INTO todo (Task, Status)
        VALUES ('{tdn}', 'Not Done');
      """)
    except:
      print(f"{tdn} already exists!")
  elif c == "2":
    tdn=input("delete which todo? ")
    cur.execute(f"DELETE FROM Todo WHERE Task='{tdn}'")
  elif c == "3":
    tdn=input("complete which todo? ")
    cur.execute(f"""
      UPDATE Todo
      SET Task = '{tdn}', Status = 'Done'
      WHERE Task = '{tdn}';
    """)
