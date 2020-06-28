import random
import sys
import time

print("British Armed Forces, Lore 3.0 Development Group \nLore Operations Console")
time.sleep(1)

UAC = input("User Authentication Code:")
UI = ""

## security block

if UAC == "administrator":
     UI = "sys_svc"

## security block end
else:
    print("Authentication Error, Terminating Process...")
    time.sleep(1)
    sys.exit


print("---------------\nWelcome, %s" % UI)


a = 0
for a in range(0, 5):
    a = a + 1
    b = ("PREPARING CONSOLE" + "." * a)
    sys.stdout.write('\r' + b)
    time.sleep(0.5)

sys.stdout.write('\r' + "Ready.")
time.sleep(0.5)

command = input("\nLOC_CONSOLE>%s >>" %UI)

operation_code = ""
operation_description = ""
outcome = ""
Secondary_Objective = ""
nextopcode = ""
nextopdesc = ""

##SECTION BREAK
oplist = ["test1", "test_1F0", "test_1F1", "test_1F2", "test_1S0", "test2", "test_2F0", "test_2F1", "test_2F2", "test_2S0"]
opdesclist = ["test1_desc", "test_1F0_desc", "test_1F1_desc", "test_1F2_desc", "test_1S0_desc", "test2_desc", "test_2F0_desc", "test_2F1_desc", "test_2F2_desc", "test_2S0_desc"]
##SECTION BREAK
if command == "run Data_Entry":
    i = 1

    while i > 0:

        def Data_Entry ():
            global operation_code
            global outcome
            global KIA
            global Secondary_Objective

            operation_code = input("CONSOLE >> Please specify the Operation Code: \nLOC_CONSOLE>%s >>" % UI)
            outcome = input("CONSOLE >> Please input the outcome in either S or F. [S]uccess / [F]ail:  \nLOC_CONSOLE>%s >>" % UI)
            KIA = int(input("CONSOLE >> Please input the percentage of KIAs compared to attendees. Round up to a natural number: \nLOC_CONSOLE>%s >>" % UI))
            Secondary_Objective = input("CONSOLE >> Please input whether or not secondary objectives were met. [Y]es / [N]o. Input Y if there were none: \nLOC_CONSOLE>%s >>" % UI)

            ## process area

            ## test1

            if operation_code == "test1" and outcome == "F":
                i = 1

            elif operation_code == "test1" and outcome == "S" and KIA >= 51:
                i = 2

            elif operation_code == "test1" and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                i = 3

            elif operation_code == "test1" and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                i = 4

            ## test2

            elif operation_code == "test2" and outcome == "F":
                i = 6

            elif operation_code == "test2" and outcome == "S" and KIA >= 51:
                i = 7

            elif operation_code == "test2" and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                i = 8

            elif operation_code == "test2" and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                i = 9

            time.sleep(0.5)
            print("Next operation: %s" % oplist[i])
            time.sleep(2)
            print("Next operation description: %s" % opdesclist[i])
            time.sleep(5)
        Data_Entry()


        continue_question = input("\nCONSOLE >> Continue? [Y/N] \nLOC_CONSOLE>%s >>" % UI)

        if continue_question == "N":
            sys.exit()
        elif continue_question == "Y":
            print("\n")

elif command == "run Brief"
    print("Welcome to the Lore 3.0 Briefing Room.")
    brief_code = input("Please input the Briefing Code provided by the Host:")

else:
    print("Shutting Down")
    sys.exit()



