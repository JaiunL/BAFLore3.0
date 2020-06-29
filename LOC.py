import random
import sys
import time

print("British Armed Forces, Lore 3.0 Development Group \nLore Operations Console")
time.sleep(1)

CL = int(input("This program requires a Clearance Level to access. Please input your Clearance Level:"))

##if statement prompt
if CL >= 3:
    UAC = input("Clearance Level 3 and higher require a User Authentication Code issued by a Sys.Ops administrator to proceed. \nPlease input your User Authentication Code:")

    if UAC == "administrator":
        UI = "Sys.Ops."
        print("Your identity has been verified. You now have Level %d permissions on this Session." % CL )

    else:
        print("Authentication Error. Shutting down.")
        time.sleep(2)
        sys.exit()

else:
    UI = "USER"

## L1 - LRs
## L2 - MRs
## L3 - HRs
## L4 - HC
## L5 - Lore Devs
## L6 - CoSC
## L7 - Sys.Ops.
## security block


## security block end


print("---------------\nWelcome, %s" % UI)

a = 0
for a in range(0, 5):
    a = a + 1
    b = ("PREPARING CONSOLE" + "." * a)
    sys.stdout.write('\r' + b)
    time.sleep(0.5)

sys.stdout.write('\r' + "Ready.")
time.sleep(0.5)

def command_module():

    command = input("\nLOC_CONSOLE>%s >>" % UI)

    operation_code = ""
    operation_description = ""
    outcome = ""
    Secondary_Objective = ""
    nextopcode = ""
    nextopdesc = ""






    ##DATABASE
    oplist = ["test1", "test_1F0", "test_1F1", "test_1F2", "test_1S0", "test2", "test_2F0", "test_2F1", "test_2F2", "test_2S0"]
    opdesclist = ["test1_desc", "test_1F0_desc", "test_1F1_desc", "test_1F2_desc", "test_1S0_desc", "test2_desc", "test_2F0_desc", "test_2F1_desc", "test_2F2_desc", "test_2S0_desc"]
    opbriefcodelist = ["tbc1", "tbc2", "tbc3", "tbc4", "tbc5", "tbc6", "tbc7", "tbc8", "tbc9", "tbc10"]
    opbrieflist = ["test1_desc", "test_1F0_desc", "test_1F1_desc", "test_1F2_desc", "test_1S0_desc", "test2_desc", "test_2F0_desc", "test_2F1_desc", "test_2F2_desc", "test_2S0_desc"]
    ##DATABASE





    if command == "run Data_Entry":
        if CL <= 3:
            print("Unauthorized Access Attempt. Terminating Session.")
            sys.exit()

        i = 1

        while i > 0:

            def Data_Entry():
                global operation_code
                global outcome
                global KIA
                global Secondary_Objective

                operation_code = input("CONSOLE >> Please specify the Operation Code: \nLOC_CONSOLE>%s >>" % UI)
                outcome = input(
                    "CONSOLE >> Please input the outcome in either S or F. [S]uccess / [F]ail:  \nLOC_CONSOLE>%s >>" % UI)
                KIA = int(input(
                    "CONSOLE >> Please input the percentage of KIAs compared to attendees. Round up to a natural number: \nLOC_CONSOLE>%s >>" % UI))
                Secondary_Objective = input(
                    "CONSOLE >> Please input whether or not secondary objectives were met. [Y]es / [N]o. Input Y if there were none: \nLOC_CONSOLE>%s >>" % UI)

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
                break
            elif continue_question == "Y":
                print("\n")

    ##BRIEF

    elif command == "run Brief":
        print(">>>>>Welcome to the Lore 3.0 Briefing Room.<<<<<")
        brief_code = input("Please input the Briefing Code provided by the Host:")

        if brief_code == "tbc1":
            i = 0
            print("Operation name: %s" % oplist[i])
            print("Description: %s" % opbrieflist[i])

    ##HELP

    elif command == "help":
        print("The following are a list of available commands, their usage, and the required Clearance Level. \n")
        print("run Data_Entry - Data-Entry module used for inputting event results - CL 3+")
        print("run Brief - Lore 3.0 Briefing Room - CL 1+")
        print("open credentials.sec - Browse UAC codes/CLs - CL 6+")
        ##print("run Overview - Lore 3.0 Storyline - CL 4+")
        ##print("run Op_Search - Lore 3.0 Operations Database - CL 3+")
        ##print("run Target_Database - Lore 3.0 Target Database - CL 1+")
        print("help - display a list of commands and a short description - CL 1+")
        print("description - display the description for this program - CL 1+")
        print("ver - version - CL 1+")
        print("whoami - display user information - CL 1+")


    ##open credentials.sec

    elif command == "open credentials.sec":
        print("format : username - UAC - Clearance Level\n")
        print("admin - administrator - L7")
        print(">>>>>END<<<<<")


    ##description

    elif command == "description":
        print("The Lore Operations Console is a component of the British Armed Forces Lore 3.0 program.\nDeveloped by Jaiun\nCredits to auto-py-to-exe for conversion\n")


    ##ver

    elif command == "ver":
        print("Version [BETA] 0.1.6, build 3\nLast Updated: 20200629")


    ##whoami

    elif command == "whoami":
        print("Username : %s" % UI)
        print("User Authentication Code : %s" % UAC)
        print("Clerance Level : %d" % CL)


    ##Exit

    else:
        print("Shutting Down")
        sys.exit()

looper = 1
while looper >= 0:
   command_module()


