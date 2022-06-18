import psycopg

def playquiz():
    try:
        with psycopg.connect(conninfo="postgresql://postgres:angjaya08102005@127.0.0.1:5432/python_quiz") as connection:
            with connection.cursor() as cursors:
                question_id = []
                option_id = []
                show_question = cursors.execute("select question, question_id, answer from quiz;")
                take_question = cursors.fetchall()
                graboption = cursors.execute("select option.question_id, option_label, option_answer from option inner join quiz on option.question_id = quiz.question_id where option.question_id = quiz.question_id;")
                printoption = cursors.fetchall()
                point = 0
                for q_id in range(len(take_question)):
                    question_id.append(take_question[q_id][1])
                for o_id in range(len(printoption)):
                    option_id.append(printoption[o_id][0])

                for main_id in range(len(question_id)):
                    print("%s. %s"%(main_id+1, take_question[main_id][0]))
                    print("Options :")
                    for checker_id in range(len(option_id)):
                        if question_id[main_id] == option_id[checker_id]:
                            print("%s. %s"%(printoption[checker_id][1], printoption[checker_id][2]))
                    print("=========================")
                    print("Point : %s\n"%(point))
                    while True:
                        useranswer = input("Your answer : ")
                        if len(useranswer) != 1:
                            print("Only option label is taken as answer.")
                            continue
                        else:
                            if useranswer.upper() == take_question[main_id][2]:
                                print("Correct, you earned a point!")
                                point += 1
                                print("Point: %s\n"%(point))
                            else:
                                print("Incorrect! Try better next question.")
                            break

                print("End of the game ! Point : %s.\nKeep it up ! See you next game."%(point))

    finally:
        if connection:
            cursors.close()
            connection.close()
