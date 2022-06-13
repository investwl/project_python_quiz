import pdb
import psycopg
from pyquiz_mainmenu import mainmenu
from pyquiz_addquestion import add_question
from pyquiz_playquiz import playquiz
#cari cara untuk supaya bisa run ini open, and all is good, i suppose. install git bash.

if __name__ == '__main__':
    print("Before playing, you have to login with your account first.")
    acc_verify = False
    userlogged = None
    passlogged = None
    with psycopg.connect(conninfo="postgresql://postgres:angjaya08102005@127.0.0.1:5432/python_quiz") as connection:
        with connection.cursor() as cursors:
            while True:
                print("A. Create account            B. Login Account")
                userinput = input("Your choice : ")
                if userinput == "A" or userinput == "a":
                    create_success = True
                    while True:
                        if create_success == False:
                            print("Cancel create account? (Yes / No)")
                            ask_cancel = input("Your answer : ")
                            if ask_cancel == "Yes" or ask_cancel == "yes":
                                break
                        newuser = input("Create username (min 3 char) : ")
                        newpass = input("Create password (min 8 char) : ")
                        if len(newuser) >= 3 and len(newpass) >= 8:
                            check_user = cursors.execute("select username from account where username = '%s';"%(newuser))
                            check_existing_user = cursors.fetchall()
                            if len(check_existing_user) > 0:
                                print("Username has already exists! Try another username.")
                                create_success = False
                                continue
                            else:
                                cursors.execute("insert into account(username, password) values('%s' , '%s');"%(newuser, newpass))
                                acc_verify = True
                                userlogged = newuser
                                passlogged = newpass
                                create_success = True
                                user_exist = False
                                print("Account successfuly created. Welcome %s."%(newuser))
                                break
                        else:
                            print("Please recheck your username or password length.")
                            create_success = False
                            continue

                elif userinput == "B" or userinput == "b":
                    login_attempt = True
                    while True:
                        if login_attempt == False:
                            ask_cancel = input("Cancel login? (Yes / No)\nYour choice : ")
                            if ask_cancel == "yes" or ask_cancel == "Yes":
                                break
                        askuser = input("Username : ")
                        askpass = input("Password : ")
                        check_username = cursors.execute("select username, password from account where username = '%s' and password = '%s';"%(askuser, askpass))
                        check_user = cursors.fetchall()
                        if len(check_user) == 1:
                            print("Access granted. Welcome %s."%(askuser))
                            acc_verify = True
                            userlogged = askuser
                            passlogged = askpass
                            break
                        else:
                            print("Incorrect username or password !")
                            login_attempt = False
                            continue
                            

                if acc_verify == True:
                    while True:
                        mainchoice = mainmenu()
                        if mainchoice == 1:
                            playquiz()
                            continue
                        elif mainchoice == 2:
                            add_question(userlogged)
                            continue
                        elif mainchoice == 3:
                            verify_login = False
                            break
                        elif mainchoice == 4:
                            import pyquiz_quizinstruction
                            continue
                        elif mainchoice == 5:
                            verify_login = True
                            break
                        elif mainchoice == 6:
                            import pyquiz_showaboutus

                if verify_login == False:
                    continue
                else:
                    break

            print("Thank you for playing the quiz")