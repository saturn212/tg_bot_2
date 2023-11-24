from loader import cursor





cursor.execute("""CREATE TABLE task
            (№ INTEGER PRIMARY KEY AUTOINCREMENT,
            id INTEGER,
            task_1 TEXT DEFAULT "-",
            task_2 TEXT DEFAULT "-",
            task_3 TEXT DEFAULT "-",
            task_4 TEXT DEFAULT "-",
            task_5 TEXT DEFAULT "-",
            task_6 TEXT DEFAULT "-",
            task_7 TEXT DEFAULT "-",
            task_8 TEXT DEFAULT "-",
            task_9 TEXT DEFAULT "-",
            task_10 TEXT DEFAULT "-")
            
""")


