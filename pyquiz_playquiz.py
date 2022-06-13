import psycopg

try:
    with psycopg.connect(conninfo="postgresql://postgres:angjaya08102005@127.0.0.1:5432/python_quiz") as connection:
        with connection.cursor() as cursors:
            def playquiz():
                show_question = cursors.execute("select question, question_id, answer from quiz;")
                take_question = cursors.fetchall()
                graboption = cursors.execute("select option.question_id, option_label, option_answer from option inner join quiz on option.question_id = quiz.question_id where option.question_id = quiz.question_id;")
                printoption = cursors.fetchall()
                point = 0
                for a in range(len(take_question)):
                    print("%s. %s"%(a+1, take_question[a][0]))
                    print("Options :")
                    for i in range(len(printoption)):
                        if printoption[i][0] == take_question[a][1]:
                            print("%s. %s"%(printoption[i][1], printoption[i][2]))
                    print("===============================")
                    print("Point : %s\n"%(point))
                    while True:
                        useranswer = input("Your answer : ")
                        if len(useranswer) != 1:
                            print("Only option label is taken as answer.")
                            continue
                        else:
                            if useranswer == take_question[a][2]:
                                print("Correct, you earned a point!")
                                point += 1
                                print("Point: %s\n"%(point))
                            else:
                                print("Incorrect! Try better next question.")
                            break

finally:
    if connection:
        cursors.close()
        connection.close()