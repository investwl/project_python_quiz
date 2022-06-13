import psycopg

try:
    with psycopg.connect(conninfo="postgresql://postgres:angjaya08102005@127.0.0.1:5432/python_quiz") as connection:
        with connection.cursor() as cursors:
            def mainmenu():
                print("============ Welcome to Trivia Quiz Game ============")
                print("1. Play Quiz\n2. Add your own questions\n3. Logout\n4. See instructions\n5. Exit\n6. About us")
                while True:
                    yourchoice = input("Enter your choice (with number): ")
                    if yourchoice.strip().isdigit():
                        choice = int(yourchoice)
                        if choice > 0 and choice < 7:
                            return choice
                        else:
                            print("Choose between 1 - 6, ordered from the list.")
                            continue
                    else:
                        print("Only numbers that are accepted in this program.")

finally:
    if connection:
        cursors.close()
        connection.close()