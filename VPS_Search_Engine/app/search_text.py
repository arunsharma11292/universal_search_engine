from app.data_base_collection import *
from app.word_comp import word_completor
from app.anylng_to_eng import live_speech_to_english
from prompt_toolkit import prompt
from app.anylng_to_eng import *
sub_Module =""
def to_return_choice_2(your_input,module_text):
    if your_input == 1:
        completer = word_completor(module_text)
        sub_Module = prompt("Type word: ", completer=completer)
    elif your_input == 2:
        sub_Module = live_speech_to_english()
        print(f"Converted (English): {sub_Module.title()}")
        sub_Module = sub_Module.title()
    return sub_Module 
def from_key_board(key_with_module_name,module):
    choice_1 = 1 if int(input("Test or voice: ")) ==1 else 2
    sub_Module = to_return_choice_2(choice_1,key_with_module_name)
    print(f"\nSearching for: {sub_Module}\n")

    if module == "Preadmission":
            if sub_Module == "Students":
                    choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                    sub_Module_2 = to_return_choice_2(choice_2,PREADMISSON_DB)
                    to_get_the_value_from_df(sub_Module_2,list_of_pre_admision)

            elif sub_Module == "Parents":
                    choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                    sub_Module_2 = to_return_choice_2(choice_2,PREADMISSON_DB)
                    to_get_the_value_from_df(sub_Module_2,list_of_pre_admision)

            elif sub_Module == "Admission":
                    choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                    sub_Module_2 = to_return_choice_2(choice_2,PREADMISSON_DB)
                    to_get_the_value_from_df(sub_Module_2,list_of_pre_admision)

            elif sub_Module == "Admin":
                    choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                    sub_Module_2 = to_return_choice_2(choice_2,PREADMISSON_DB)
                    to_get_the_value_from_df(sub_Module_2,list_of_pre_admision)

            elif sub_Module == "Office":
                    choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                    sub_Module_2 = to_return_choice_2(choice_2,PREADMISSON_DB)
                    to_get_the_value_from_df(sub_Module_2,list_of_pre_admision)

            elif sub_Module == "Faculty":
                    choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                    sub_Module_2 = to_return_choice_2(choice_2,PREADMISSON_DB)
                    to_get_the_value_from_df(sub_Module_2,list_of_pre_admision)

            elif sub_Module == "Interview Panel":
                    choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                    sub_Module_2 = to_return_choice_2(choice_2,PREADMISSON_DB)
                    to_get_the_value_from_df(sub_Module_2,list_of_pre_admision)

            elif sub_Module == "Finance Team":
                    choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                    sub_Module_2 = to_return_choice_2(choice_2,PREADMISSON_DB)
                    to_get_the_value_from_df(sub_Module_2,list_of_pre_admision)

            elif sub_Module == "Management":
                    choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                    sub_Module_2 = to_return_choice_2(choice_2,PREADMISSON_DB)
                    to_get_the_value_from_df(sub_Module_2,list_of_pre_admision)

            elif sub_Module == "Head of Institution":
                    choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                    sub_Module_2 = to_return_choice_2(choice_2,PREADMISSON_DB)
                    to_get_the_value_from_df(sub_Module_2,list_of_pre_admision)

            else:
                print("Invalid Input")

    if module == "Admission" or module == "Entry":
            if sub_Module == "Students":
                    choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                    sub_Module_2 = to_return_choice_2(choice_2,ADMISSION_DB)
                    to_get_the_value_from_df(sub_Module_2,list_of_admision)

            elif sub_Module == "Parents":
                    choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                    sub_Module_2 = to_return_choice_2(choice_2,ADMISSION_DB)
                    to_get_the_value_from_df(sub_Module_2,list_of_admision)

            elif sub_Module == "Admission Office":
                    choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                    sub_Module_2 = to_return_choice_2(choice_2,ADMISSION_DB)
                    to_get_the_value_from_df(sub_Module_2,list_of_admision)

            elif sub_Module == "Admin Staff":
                    choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                    sub_Module_2 = to_return_choice_2(choice_2,ADMISSION_DB)
                    to_get_the_value_from_df(sub_Module_2,list_of_admision)

            elif sub_Module == "Faculty":
                    choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                    sub_Module_2 = to_return_choice_2(choice_2,ADMISSION_DB)
                    to_get_the_value_from_df(sub_Module_2,list_of_admision)

            elif sub_Module == "Interview Panel":
                    choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                    sub_Module_2 = to_return_choice_2(choice_2,ADMISSION_DB)
                    to_get_the_value_from_df(sub_Module_2,list_of_admision)

            elif sub_Module == "Management":
                    choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                    sub_Module_2 = to_return_choice_2(choice_2,ADMISSION_DB)
                    to_get_the_value_from_df(sub_Module_2,list_of_admision)

            elif sub_Module == "Leadership":
                    choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                    sub_Module_2 = to_return_choice_2(choice_2,ADMISSION_DB)
                    to_get_the_value_from_df(sub_Module_2,list_of_admision)

            else:
                print("Invalid Input")

    elif module == "Fees" or module =="Charges":
        if sub_Module == "Students":
                    choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                    sub_Module_2 = to_return_choice_2(choice_2,FEES_DB)
                    to_get_the_value_from_df(sub_Module_2,list_of_fees)
        elif sub_Module == "Parents":
                choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                sub_Module_2 = to_return_choice_2(choice_2,FEES_DB)
                to_get_the_value_from_df(sub_Module_2,list_of_fees)

        elif sub_Module == "Fees Office":
                choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                sub_Module_2 = to_return_choice_2(choice_2,FEES_DB)
                to_get_the_value_from_df(sub_Module_2,list_of_fees)

        elif sub_Module == "Admin Staff":
                choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                sub_Module_2 = to_return_choice_2(choice_2,FEES_DB)
                to_get_the_value_from_df(sub_Module_2,list_of_fees)

        elif sub_Module == "Finance":
                choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                sub_Module_2 = to_return_choice_2(choice_2,FEES_DB)
                to_get_the_value_from_df(sub_Module_2,list_of_fees)

        elif sub_Module == "Accounts Teams":
                choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                sub_Module_2 = to_return_choice_2(choice_2,FEES_DB)
                to_get_the_value_from_df(sub_Module_2,list_of_fees)

        else:
            print("Invalid Input")
            
    elif module == "Exam":
        if sub_Module == "Configuration":
                    choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                    sub_Module_2 = to_return_choice_2(choice_2,EXAM_DB)
                    to_get_the_value_from_df(sub_Module_2,list_of_Exam)

        elif sub_Module == "Master":
                choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                sub_Module_2 = to_return_choice_2(choice_2,EXAM_DB)
                to_get_the_value_from_df(sub_Module_2,list_of_Exam)

        elif sub_Module == "Exam Mapping":
                choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                sub_Module_2 = to_return_choice_2(choice_2,EXAM_DB)
                to_get_the_value_from_df(sub_Module_2,list_of_Exam)

        elif sub_Module == "Marks Entry":
                choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                sub_Module_2 = to_return_choice_2(choice_2,EXAM_DB)
                to_get_the_value_from_df(sub_Module_2,list_of_Exam)

        elif sub_Module == "Reports":
                choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                sub_Module_2 = to_return_choice_2(choice_2,EXAM_DB)
                to_get_the_value_from_df(sub_Module_2,list_of_Exam)

        elif sub_Module == "Students":
                choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                sub_Module_2 = to_return_choice_2(choice_2,EXAM_DB)
                to_get_the_value_from_df(sub_Module_2,list_of_Exam)
        else:
            print("Invalid Input")

    elif module == "HRMS":
        if sub_Module == "Master":
                    choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                    sub_Module_2 = to_return_choice_2(choice_2,HRMS_DB)
                    to_get_the_value_from_df(sub_Module_2,list_of_HRMS)

        elif sub_Module == "Employee":
                choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                sub_Module_2 = to_return_choice_2(choice_2,HRMS_DB)
                to_get_the_value_from_df(sub_Module_2,list_of_HRMS)

        elif sub_Module == "Transaction":
                choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                sub_Module_2 = to_return_choice_2(choice_2,HRMS_DB)
                to_get_the_value_from_df(sub_Module_2,list_of_HRMS)

        elif sub_Module == "Reports":
                choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                sub_Module_2 = to_return_choice_2(choice_2,HRMS_DB)
                to_get_the_value_from_df(sub_Module_2,list_of_HRMS)
        else:
            print("Invalid Input")

    elif module == "Inventory":
        if sub_Module == "Master":
                    choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                    sub_Module_2 = to_return_choice_2(choice_2,INVENTORY_DB)
                    to_get_the_value_from_df(sub_Module_2,list_of_Inventory)

        elif sub_Module == "Transaction":
                choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                sub_Module_2 = to_return_choice_2(choice_2,INVENTORY_DB)
                to_get_the_value_from_df(sub_Module_2,list_of_Inventory)

        elif sub_Module == "Reports":
                choice_2 = 1 if int(input("Test or voice: ")) ==1 else 2
                sub_Module_2 = to_return_choice_2(choice_2,INVENTORY_DB)
                to_get_the_value_from_df(sub_Module_2,list_of_Inventory)
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")            
