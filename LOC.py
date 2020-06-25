import random
import sys
import time

print("British Armed Forces, Lore 3.0 Development Group \nLore Operations Console")
time.sleep(1)

UAC = input("User Authentication Code:")
UI = ""

if UAC == "f29132de8ee257d6f4c3ff8459681219":
    UI = "[PRG] Jaiun - 7917"

elif UAC == "2fc76ade25d67d6a566ac74173e1775a":
    UI = "[CDS] W_olfIron - 5254"

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

if command == "run LOC_module":
    i = 1

    while i > 0:

        operation_code = input("CONSOLE >> Please specify the Operation Code: \nLOC_CONSOLE>%s >>" % UI)
        operation_description = ""
        outcome = ""

        ##SECTION BREAK



        if operation_code == "test1":
            outcome = input("CONSOLE >> Please input the outcome in either S or F. [S]uccess / [F]ail:  \nLOC_CONSOLE>%s >>" % UI)
            KIA = int(input("CONSOLE >> Please input the percentage of KIAs compared to attendees. Round up to a natural number: \nLOC_CONSOLE>%s >>" % UI))
            Secondary_Objective = input("CONSOLE >> Please input whether or not secondary objectives were met. [Y]es / [N]o. Input Y if there were none: \nLOC_CONSOLE>%s >>" % UI)

            if outcome == "F":
                operation_code = "test_F0"

            elif outcome == "S":
                if KIA >= 50:
                    operation_code = "test_F1"
                elif KIA <= 50:
                    if Secondary_Objective == "Y":
                        operation_code = "test_S1"
                    elif Secondary_Objective == "N":
                        operation_code = "test_F2"

        if operation_code == "test1":
            operation_description = "test1_desc"

        elif operation_code == "test_F0":
            operation_description = "testF0_desc"

        elif operation_code == "test_F1":
            operation_description = "testF1_desc"

        elif operation_code == "test_F2":
            operation_description = "testF2_desc"

        elif operation_code == "test_S1":
            operation_description = "testS1_desc"

        else:
            print("Taft")
            sys.exit()

        print("CONSOLE >> Next Operation: %s" % operation_code )
        time.sleep(2)
        print("CONSOLE >> Description: %s" % operation_description)
        time.sleep(5)

        continue_question = input("\nCONSOLE >> Continue? [Y/N] \nLOC_CONSOLE>%s >>" % UI)

        if continue_question == "N":
            sys.exit()
        elif continue_question == "Y":
            print("\n")

else:
    print("Shutting Down")
    sys.exit()



