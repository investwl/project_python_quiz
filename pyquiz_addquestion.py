import psycopg

def opening_question():
    if_cancel = False
    print("Welcome to adding question section.")
    print("Add your question below or just type in 'cancel' to cancel adding question")
    userquestion = input("Your question : ")
    if userquestion.lower() == "cancel":
        if_cancel = True
    return if_cancel, userquestion

def fill_question(option_library):
    option_library_answer = []
    for a in range(len(option_library)):
        print("Input the option for your question with maximum of 5 options.")
        print("Type in 'done' to finish adding option")
        useroption = input("%s. "%(option_library[a]))
        if useroption.lower() == "done":
            break
        option_library_answer.append(useroption)
    return option_library_answer

def add_question(userlogged):
    try:
        with psycopg.connect(conninfo="postgresql://postgres:angjaya08102005@127.0.0.1:5432/python_quiz") as connection:
            with connection.cursor() as cursors:
                while True:
                    opening_quiz = opening_question()
                    if opening_quiz[0] == True:
                        return None
                    get_user_id = cursors.execute("select user_id from account where username = '%s';"%(userlogged))
                    get_user = cursors.fetchone()
                    option_library = ["A", "B", "C", "D", "E"]
                    while True:
                        fill_quiz = fill_question(option_library)
                        if len(fill_quiz) >= 2:
                            print(fill_quiz)
                            print("Which option is the answer? (only input the ABCs)")
                            question_answer = input("The answer : ")
                            break
                        else:
                            print("Minimum 2 options! Example : True or False.")
                            continue

                    print("Add more question?")
                    more_question = input("Yes / No? : ")
                    if more_question.lower() == "no":
                        print("Thanks for adding your questions !")
                        
                        break
                
    finally:
        if connection:
            cursors.close()
            connection.close()

    return fill_quiz, opening_quiz[1], get_user[0], option_library, question_answer.upper()
    

def fill_answer(option_library_answer, userquestion, get_user, option_library, question_answer):
    try:
        with psycopg.connect(conninfo="postgresql://postgres:angjaya08102005@127.0.0.1:5432/python_quiz") as connection:
            with connection.cursor() as cursors:
                for a in range(len(option_library_answer)):
                    if question_answer.upper() == option_library[a][0]:
                        insert_table = cursors.execute("insert into quiz(question, answer, user_id) values('%s', '%s', '%s') returning question_id;"%(userquestion, question_answer, get_user))
                        return_insert = cursors.fetchone()
                        for b in range(len(option_library_answer)):
                            insert_question = cursors.execute("insert into option(question_id, option_label, option_answer) values('%s', '%s', '%s');"%(return_insert[0], option_library[b], option_library_answer[b]))
                        print("Question successfuly added !\n===================")
    finally:
        if connection:
            cursors.close()
            connection.close()
