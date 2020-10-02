import sys
import time
import random

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
    oplist = ["test1", "test_1F0", "test_1F1", "test_1F2", "test_1S0", "test2", "test_2F0", "test_2F1", "test_2F2", "test_2S0", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    b2oplist = ["Operation Yeet", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    b3oplist = ["1", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    b4oplist = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    b5oplist = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    b6oplist = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    b7oplist = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    b8oplist = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

    desclist = ["test1_desc", "test_1F0_desc", "test_1F1_desc", "test_1F2_desc", "test_1S0_desc", "test2_desc", "test_2F0_desc", "test_2F1_desc", "test_2F2_desc", "test_2S0_desc", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    b2desclist = ["yeeting will need to be done", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    b3desclist = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    b4desclist = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    b5desclist = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    b6desclist = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    b7desclist = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    b8desclist = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

    codelist = ["tbc1", "tbc2", "tbc3", "tbc4", "tbc5", "tbc6", "tbc7", "tbc8", "tbc9", "tbc10", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    b2codelist = ["yeet", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    b3codelist = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    b4codelist = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    b5codelist = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    b6codelist = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    b7codelist = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    b8codelist = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

    brieflist = ["test1_desc", "test_1F0_desc", "test_1F1_desc", "test_1F2_desc", "test_1S0_desc", "test2_desc", "test_2F0_desc", "test_2F1_desc", "test_2F2_desc", "test_2S0_desc"]
    b2brieflist = ["We will yeet bruni off a cliff.", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    b3brieflist = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    b4brieflist = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    b5brieflist = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    b6brieflist = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    b7brieflist = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    bb8rieflist = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    
    tarlist_people = ["Black", "White", "Blue", "Green"]
    tarlist_vehicle = ["V1", "V2", "V3"]

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

                ## op 1 results
                if operation_code == oplist[0] and outcome == "F":
                    i = 1

                elif operation_code == oplist[0] and outcome == "S" and KIA >= 51:
                    i = 1

                elif operation_code == oplist[0] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 2

                elif operation_code == oplist[0] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 3

                ## op 2-1 results
                elif operation_code == oplist[1] and outcome == "F":
                    i = 4

                elif operation_code == oplist[1] and outcome == "S" and KIA >= 51:
                    i = 4

                elif operation_code == oplist[1] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 5

                elif operation_code == oplist[1] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 6

                ## op 2-2 results
                elif operation_code == oplist[2] and outcome == "F":
                    i = 7

                elif operation_code == oplist[2] and outcome == "S" and KIA >= 51:
                    i = 7

                elif operation_code == oplist[2] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 8

                elif operation_code == oplist[2] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 9

                ## op 2-3 results
                elif operation_code == oplist[3] and outcome == "F":
                    i = 10

                elif operation_code == oplist[3] and outcome == "S" and KIA >= 51:
                    i = 10

                elif operation_code == oplist[3] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 11

                elif operation_code == oplist[3] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 12

                ## op 3-1 results
                elif operation_code == oplist[4] and outcome == "F":
                    i = 13

                elif operation_code == oplist[4] and outcome == "S" and KIA >= 51:
                    i = 13

                elif operation_code == oplist[4] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 14

                elif operation_code == oplist[4] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 15

                ## op 3-2 results
                elif operation_code == oplist[5] and outcome == "F":
                    i = 16

                elif operation_code == oplist[5] and outcome == "S" and KIA >= 51:
                    i = 16

                elif operation_code == oplist[5] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 17

                elif operation_code == oplist[5] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 18

                ## op 3-3 results
                elif operation_code == oplist[6] and outcome == "F":
                    i = 19

                elif operation_code == oplist[6] and outcome == "S" and KIA >= 51:
                    i = 19

                elif operation_code == oplist[6] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 20

                elif operation_code == oplist[6] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 21

                ## op 3-4 results
                elif operation_code == oplist[7] and outcome == "F":
                    i = 22

                elif operation_code == oplist[7] and outcome == "S" and KIA >= 51:
                    i = 22

                elif operation_code == oplist[7] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 23

                elif operation_code == oplist[7] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 24

                ## op 3-5 results
                elif operation_code == oplist[8] and outcome == "F":
                    i = 25

                elif operation_code == oplist[8] and outcome == "S" and KIA >= 51:
                    i = 25

                elif operation_code == oplist[8] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 26

                elif operation_code == oplist[8] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 27

                ## op 3-6 results
                elif operation_code == oplist[9] and outcome == "F":
                    i = 28

                elif operation_code == oplist[9] and outcome == "S" and KIA >= 51:
                    i = 28

                elif operation_code == oplist[9] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 29

                elif operation_code == oplist[9] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 30

                ## op 3-7 results
                elif operation_code == oplist[10] and outcome == "F":
                    i = 31

                elif operation_code == oplist[10] and outcome == "S" and KIA >= 51:
                    i = 31

                elif operation_code == oplist[10] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 32

                elif operation_code == oplist[10] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 33

                ## op 3-8 results
                elif operation_code == oplist[11] and outcome == "F":
                    i = 34

                elif operation_code == oplist[11] and outcome == "S" and KIA >= 51:
                    i = 34

                elif operation_code == oplist[11] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 35

                elif operation_code == oplist[11] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 36

                ##op 3-9 results
                elif operation_code == oplist[12] and outcome == "F":
                    i = 37

                elif operation_code == oplist[12] and outcome == "S" and KIA >= 51:
                    i = 37

                elif operation_code == oplist[12] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 38

                elif operation_code == oplist[12] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 39




                ## Branch 2

                ## op 1 results
                if operation_code == b2oplist[0] and outcome == "F":
                    i = 1

                elif operation_code == b2oplist[0] and outcome == "S" and KIA >= 51:
                    i = 1

                elif operation_code == b2oplist[0] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 2

                elif operation_code == b2oplist[0] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 3

                ## op 2-1 results
                elif operation_code == b2oplist[1] and outcome == "F":
                    i = 4

                elif operation_code == b2oplist[1] and outcome == "S" and KIA >= 51:
                    i = 4

                elif operation_code == b2oplist[1] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 5

                elif operation_code == b2oplist[1] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 6

                ## op 2-2 results
                elif operation_code == b2oplist[2] and outcome == "F":
                    i = 7

                elif operation_code == b2oplist[2] and outcome == "S" and KIA >= 51:
                    i = 7

                elif operation_code == b2oplist[2] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 8

                elif operation_code == b2oplist[2] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 9

                ## op 2-3 results
                elif operation_code == b2oplist[3] and outcome == "F":
                    i = 10

                elif operation_code == b2oplist[3] and outcome == "S" and KIA >= 51:
                    i = 10

                elif operation_code == b2oplist[3] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 11

                elif operation_code == b2oplist[3] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 12

                ## op 3-1 results
                elif operation_code == b2oplist[4] and outcome == "F":
                    i = 13

                elif operation_code == b2oplist[4] and outcome == "S" and KIA >= 51:
                    i = 13

                elif operation_code == b2oplist[4] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 14

                elif operation_code == b2oplist[4] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 15

                ## op 3-2 results
                elif operation_code == b2oplist[5] and outcome == "F":
                    i = 16

                elif operation_code == b2oplist[5] and outcome == "S" and KIA >= 51:
                    i = 16

                elif operation_code == b2oplist[5] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 17

                elif operation_code == b2oplist[5] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 18

                ## op 3-3 results
                elif operation_code == b2oplist[6] and outcome == "F":
                    i = 19

                elif operation_code == b2oplist[6] and outcome == "S" and KIA >= 51:
                    i = 19

                elif operation_code == b2oplist[6] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 20

                elif operation_code == b2oplist[6] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 21

                ## op 3-4 results
                elif operation_code == b2oplist[7] and outcome == "F":
                    i = 22

                elif operation_code == b2oplist[7] and outcome == "S" and KIA >= 51:
                    i = 22

                elif operation_code == b2oplist[7] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 23

                elif operation_code == b2oplist[7] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 24

                ## op 3-5 results
                elif operation_code == b2oplist[8] and outcome == "F":
                    i = 25

                elif operation_code == b2oplist[8] and outcome == "S" and KIA >= 51:
                    i = 25

                elif operation_code == b2oplist[8] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 26

                elif operation_code == b2oplist[8] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 27

                ## op 3-6 results
                elif operation_code == b2oplist[9] and outcome == "F":
                    i = 28

                elif operation_code == b2oplist[9] and outcome == "S" and KIA >= 51:
                    i = 28

                elif operation_code == b2oplist[9] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 29

                elif operation_code == b2oplist[9] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 30

                ## op 3-7 results
                elif operation_code == b2oplist[10] and outcome == "F":
                    i = 31

                elif operation_code == b2oplist[10] and outcome == "S" and KIA >= 51:
                    i = 31

                elif operation_code == b2oplist[10] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 32

                elif operation_code == b2oplist[10] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 33

                ## op 3-8 results
                elif operation_code == b2oplist[11] and outcome == "F":
                    i = 34

                elif operation_code == b2oplist[11] and outcome == "S" and KIA >= 51:
                    i = 34

                elif operation_code == b2oplist[11] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 35

                elif operation_code == b2oplist[11] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 36

                ##op 3-9 results
                elif operation_code == b2oplist[12] and outcome == "F":
                    i = 37

                elif operation_code == b2oplist[12] and outcome == "S" and KIA >= 51:
                    i = 37

                elif operation_code == b2oplist[12] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 38

                elif operation_code == b2oplist[12] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 39



                ## Branch 3
                ## op 1 results
                if operation_code == b3oplist[0] and outcome == "F":
                    i = 1

                elif operation_code == b3oplist[0] and outcome == "S" and KIA >= 51:
                    i = 1

                elif operation_code == b3oplist[0] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 2

                elif operation_code == b3oplist[0] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 3

                ## op 2-1 results
                elif operation_code == b3oplist[1] and outcome == "F":
                    i = 4

                elif operation_code == b3oplist[1] and outcome == "S" and KIA >= 51:
                    i = 4

                elif operation_code == b3oplist[1] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 5

                elif operation_code == b3oplist[1] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 6

                ## op 2-2 results
                elif operation_code == b3oplist[2] and outcome == "F":
                    i = 7

                elif operation_code == b3oplist[2] and outcome == "S" and KIA >= 51:
                    i = 7

                elif operation_code == b3oplist[2] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 8

                elif operation_code == b3oplist[2] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 9

                ## op 2-3 results
                elif operation_code == b3oplist[3] and outcome == "F":
                    i = 10

                elif operation_code == b3oplist[3] and outcome == "S" and KIA >= 51:
                    i = 10

                elif operation_code == b3oplist[3] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 11

                elif operation_code == b3oplist[3] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 12

                ## op 3-1 results
                elif operation_code == b3oplist[4] and outcome == "F":
                    i = 13

                elif operation_code == b3oplist[4] and outcome == "S" and KIA >= 51:
                    i = 13

                elif operation_code == b3oplist[4] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 14

                elif operation_code == b3oplist[4] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 15

                ## op 3-2 results
                elif operation_code == b3oplist[5] and outcome == "F":
                    i = 16

                elif operation_code == b3oplist[5] and outcome == "S" and KIA >= 51:
                    i = 16

                elif operation_code == b3oplist[5] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 17

                elif operation_code == b3oplist[5] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 18

                ## op 3-3 results
                elif operation_code == b3oplist[6] and outcome == "F":
                    i = 19

                elif operation_code == b3oplist[6] and outcome == "S" and KIA >= 51:
                    i = 19

                elif operation_code == b3oplist[6] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 20

                elif operation_code == b3oplist[6] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 21

                ## op 3-4 results
                elif operation_code == b3oplist[7] and outcome == "F":
                    i = 22

                elif operation_code == b3oplist[7] and outcome == "S" and KIA >= 51:
                    i = 22

                elif operation_code == b3oplist[7] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 23

                elif operation_code == b3oplist[7] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 24

                ## op 3-5 results
                elif operation_code == b3oplist[8] and outcome == "F":
                    i = 25

                elif operation_code == b3oplist[8] and outcome == "S" and KIA >= 51:
                    i = 25

                elif operation_code == b3oplist[8] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 26

                elif operation_code == b3oplist[8] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 27

                ## op 3-6 results
                elif operation_code == b3oplist[9] and outcome == "F":
                    i = 28

                elif operation_code == b3oplist[9] and outcome == "S" and KIA >= 51:
                    i = 28

                elif operation_code == b3oplist[9] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 29

                elif operation_code == b3oplist[9] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 30

                ## op 3-7 results
                elif operation_code == b3oplist[10] and outcome == "F":
                    i = 31

                elif operation_code == b3oplist[10] and outcome == "S" and KIA >= 51:
                    i = 31

                elif operation_code == b3oplist[10] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 32

                elif operation_code == b3oplist[10] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 33

                ## op 3-8 results
                elif operation_code == b3oplist[11] and outcome == "F":
                    i = 34

                elif operation_code == b3oplist[11] and outcome == "S" and KIA >= 51:
                    i = 34

                elif operation_code == b3oplist[11] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 35

                elif operation_code == b3oplist[11] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 36

                ##op 3-9 results
                elif operation_code == b3oplist[12] and outcome == "F":
                    i = 37

                elif operation_code == b3oplist[12] and outcome == "S" and KIA >= 51:
                    i = 37

                elif operation_code == b3oplist[12] and outcome == "S" and KIA <= 50 and Secondary_Objective == "N":
                    i = 38

                elif operation_code == b3oplist[12] and outcome == "S" and KIA <= 50 and Secondary_Objective == "Y":
                    i = 39





                if operation_code in oplist:
                    time.sleep(0.5)
                    print("Next operation: Operation %s" % oplist[i])
                    time.sleep(2)
                    print("Operation Code: " + codelist[i])
                    time.sleep(2)
                    print("Next operation description: %s" % desclist[i])
                    time.sleep(5)

                elif operation_code in b2oplist:
                    time.sleep(0.5)
                    print("Next operation: Operation %s" % b2oplist[i])
                    time.sleep(2)
                    print("Operation Code: " + b2codelist[i])
                    time.sleep(2)
                    print("Next operation description: %s" % b2desclist[i])
                    time.sleep(5)

                elif operation_code in b3oplist:
                    time.sleep(0.5)
                    print("Next operation: Operation %s" % b2oplist[i])
                    time.sleep(2)
                    print("Operation Code: " + b3codelist[i])
                    time.sleep(2)
                    print("Next operation description: %s" % b2desclist[i])
                    time.sleep(5)

            Data_Entry()

            continue_question = input("\nCONSOLE >> Continue? [Y/N] \nLOC_CONSOLE>%s >>" % UI)

            if continue_question == "N":
                print("Shutting Down")
                sys.exit()
            elif continue_question == "Y":
                print("\n")

    ##BRIEF

    elif command == "run Brief":
        print("Welcome to the Lore 3.0 Briefing Room.")
        brief_code = input("Please input the Briefing Code provided by the Host:")

        if brief_code in codelist:
            index1 = oplist.index(brief_code)
            print("Operation name: %s" % oplist[index1])
            print("Brief: %s" % brieflist[index1])
            print("Description: %s" % desclist[index1])

        elif brief_code in b2codelist:
            index1 = b2oplist.index(brief_code)
            print("Operation name: %s" % b2oplist[index1])
            print("Brief: %s" % b2brieflist[index1])
            print("Description: %s" % b2desclist[index1])

        elif brief_code in b3codelist:
            index1 = b2oplist.index(brief_code)
            print("Operation name: %s" % b2oplist[index1])
            print("Brief: %s" % b2brieflist[index1])
            print("Description: %s" % b2desclist[index1])



    ##HELP

    elif command == "help":
        print("The following are a list of available commands, their usage, and the required Clearance Level. \n")
        print("run Data_Entry - Data-Entry module used for inputting event results - CL 3+") #done
        print("run Brief - Lore 3.0 Briefing Room - CL 1+") #done
        print("open credentials.sec - Browse UAC codes/CLs - CL 6+") #done
        ##print("run Overview - Lore 3.0 Storyline - CL 4+")
        print("run Op_Search - Lore 3.0 Operations Database - CL 3+") #done
        ##print("run Target_Database - Lore 3.0 Target Database - CL 1+")
        print("help - display a list of commands and a short description - CL 1+") #done
        print("description - display the description for this program - CL 1+") #done
        print("ver - version - CL 1+") #done
        print("whoami - display user information - CL 1+") #done


    ##open credentials.sec

    elif command == "open credentials.sec":
        
        if CL <= 4:
            print("ERROR 401 - UNAUTHORIZED/nYou do not have sufficient permissions to run this command. Shutting down.")
            time.sleep(0.7)
            sys.exit()
            
        
        print("format : username - UAC - Clearance Level\n")
        print("admin - administrator - L7")
        print(">>>>>END<<<<<")


    ##description

    elif command == "description":
        print("The Lore Operations Console is a component of the British Armed Forces Lore 3.0 program.\nDeveloped by Jaiun, Newwly\nCredits to auto-py-to-exe for exe conversion\n")


    ##ver

    elif command == "ver":
        print("Version [BETA] 0.1.6, build 3\nLast Updated: 20200629")


    ##whoami

    elif command == "whoami":
        print("Username : %s" % UI)
        print("User Authentication Code : %s" % UAC)
        print("Clearance Level : %d" % CL)


    ##op_search
    elif command == "run Op_Search":
        opname = input("Welcome to Operation Search, please input the name of the operation you would like details on (with capitalization):")



        if opname in oplist:
            index = oplist.index(opname)
            sys.stdout.write(opname + " found, fetching description. ")
            time.sleep(1)
            sys.stdout.write("\n" + opname + " - Description:\n" + desclist[index])

        elif opname in b2oplist:
            index = b2oplist.index(opname)
            sys.stdout.write(opname + " found, fetching description. ")
            time.sleep(1)
            sys.stdout.write("\n" + opname + " - Description:\n" + b2desclist[index])

        elif opname in b3oplist:
            index = b3oplist.index(opname)
            sys.stdout.write(opname + " found, fetching description. ")
            time.sleep(1)
            sys.stdout.write("\n" + opname + " - Description:\n" + b3desclist[index])


        else:
            time.sleep(1.5)
            sys.stdout.write("Operation name not found.")
            time.sleep(1.5)
            sys.stdout.write("\r" + "Redirecting to command module.\n")
            time.sleep(1.5)
            for a in range(0, 5):
                a = a + 1
                b = ("." * a)
                sys.stdout.write('\r' + b)
                time.sleep(0.4)

    ##run Target_Database
    
    tarlist_people

    elif command == "run Target_Database":
        print("Welcome to the British Armed Forces Target Database. Please select the type of the target you wish to search and input the number.")
        print("People - input [1]\nVehicles - input [2]\nBuildings/Locations - input[3]")
        tartype = int(input("LOC_CONSOLE>%s >>" % UI))
        
        if tartype == 1:
            print(*tarlist_people, sep = ", ")
            target = input("Input the name of the target would you like to view")
        
        
     

    ##Exit

    else:
        print("Shutting Down")
        sys.exit()


looper = 1
while looper >= 0:
   command_module()
