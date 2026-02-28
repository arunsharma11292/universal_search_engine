from app.data_base_collection import *
dictionay_of_db_with_module = {
    "Admission": {"Master":"","College":"","Documents":"","Student":"","Attendance":"",
                  "Subjects":"","Course":""},
    "Preadmission": {"Marks": "", "Master": "","Caste":"","Fees_Payment":"","Registration":""},
    "Fees": {"Master":"","Payment":"","Temp":"","Concession":"","Category":"","Mapping":"",
             "Feedback":"","Student":"","FeeClassWiseDetails":"","Transaction":""},
    "Exam": {"Student":"","Marks":"","SKILLS":"","Subject":"","Yearly":"","Exams":"",
             "Session":"","Users":"","Yrly":"","Login":"","College":"","Activities":"","Course":""},
    "Inventory": {"Master":"","Temp":"","Stock":"","Purchase":"","Payment":"","Asset":"","Return":"",
                  "Tax":"","Sales":"","Store":"","Student":"","Department":""},
    "HRMS": {"Master":"","Employee":"","Management":"","Authorisation":"","Training":""}
}

def categroise_table_as_module():
    for key, val in dict_of_all_modules.items():

        if key == "Preadmission_":
            marks = [i for i in val if "Marks" in i]
            master = [j for j in val if "Master" in j]
            caste = [k for k in val if "caste" in k]
            fees_pay = [l for l in val if "Fee_" in l]
            registration = [m for m in val if "Registration_" in m]

            dictionay_of_db_with_module["Preadmission"].update({
                "Marks": marks,
                "Master": master,
                "Caste" :caste,
                "Fees_Payment" :fees_pay,
                "Registration" :registration
            })
        elif key == "Adm_":
            master_adm = [i for i in val if "Master" in i]
            college_adm = [j for j in val if "College" in j]
            documents_adm = [k for k in val if "Documents" in k]
            student_adm = [l for l in val if "Student" in l]
            attendance_adm = [m for m in val if "Attendance" in m]
            subjects_adm = [n for n in val if "Subjects" in n]
            Course_adm = [o for o in val if "Course" in o]

            dictionay_of_db_with_module["Admission"].update({
                "Master": master_adm,
                "College": college_adm,
                "Documents" :documents_adm,
                "Student" :student_adm,
                "Attendance" :attendance_adm,
                "Subjects" :subjects_adm,
                "Course" :Course_adm
            })

        elif key == "Fee":
            master_fee = [i for i in val if "Master" in i]
            payment_fee = [j for j in val if "Payment" in j]
            temp_fee = [k for k in val if "Temp" in k]
            concession_fee = [l for l in val if "Concession" in l]
            category_fee = [m for m in val if "Category" in m]
            mapping_fee = [n for n in val if "Mapping" in n]
            feedback_fee = [o for o in val if "Feedback" in o]
            student_fee = [p for p in val if "Student" in p]
            feeClassWiseDetails_fee = [q for q in val if "FeeClassWiseDetails" in q]
            transaction_fee = [r for r in val if "Transaction" in r]

            dictionay_of_db_with_module["Fees"].update({
                "Master": master_fee,
                "Payment": payment_fee,
                "Temp" :temp_fee,
                "Concession" :concession_fee,
                "Category" :category_fee,
                "Mapping" :mapping_fee,
                "Feedback" :feedback_fee,
                "Student" :student_fee,
                "FeeClassWiseDetails":feeClassWiseDetails_fee,
                "Transaction":transaction_fee
            })

        elif key == "Exm_":
            student_exm = [i for i in val if "Student" in i]
            marks_exm = [j for j in val if "Marks" in j]
            skills_exm = [k for k in val if "SKILLS" in k]
            subject_exm = [l for l in val if "Subject" in l]
            yearly_exm = [m for m in val if "Yearly" in m]
            exams_exm = [n for n in val if "Exams" in n]
            session_exm = [o for o in val if "Session" in o]
            users_exm = [p for p in val if "Users" in p]
            yrly_exm = [q for q in val if "Yrly" in q]
            login_exm = [r for r in val if "Login" in r]
            college_exm = [s for s in val if "College" in s]
            activities_exm = [s for s in val if "Activities" in s]
            course_exm = [s for s in val if "Course" in s]

            dictionay_of_db_with_module["Exam"].update({
                "Student": student_exm,
                "Marks": marks_exm,
                "SKILLS" :skills_exm,
                "Subject" :subject_exm,
                "Yearly" :yearly_exm,
                "Exams" :exams_exm,
                "Session" :session_exm,
                "Users" :users_exm,
                "Yrly":yrly_exm,
                "Login":login_exm,
                "College":college_exm,
                "Activities":activities_exm,
                "Course":course_exm
            })

        elif key == "INV_":
            master_inv = [i for i in val if "Master" in i]
            temp_inv = [j for j in val if "Temp" in j]
            stock_inv = [k for k in val if "Stock" in k]
            purchase_inv = [l for l in val if "Purchase" in l]
            payment_inv = [m for m in val if "Payment" in m]
            asset_inv = [n for n in val if "Asset" in n]
            return_inv = [o for o in val if "Return" in o]
            tax_inv = [p for p in val if "Tax" in p]
            sales_inv = [q for q in val if "Sales" in q]
            store_inv = [r for r in val if "Store" in r]
            student_inv = [s for s in val if "Student" in s]
            department_inv = [s for s in val if "Department" in s]


            dictionay_of_db_with_module["Inventory"].update({
                "Master": master_inv,
                "Temp": temp_inv,
                "Stock" :stock_inv,
                "Purchase" :purchase_inv,
                "Payment" :payment_inv,
                "Asset" :asset_inv,
                "Return" :return_inv,
                "Tax" :tax_inv,
                "Sales":sales_inv,
                "Store":store_inv,
                "Student":student_inv,
                "Department":department_inv
            })
        elif key == "HR_":
            master_hrms = [i for i in val if "Master" in i]
            employee_hrms = [j for j in val if "Employee" in j]
            management_hrms = [k for k in val if "Management" in k]
            authorisation_hrms = [l for l in val if "Auth" in l]
            training_hrms = [m for m in val if "Training" in m]

            dictionay_of_db_with_module["HRMS"].update({
                "Master": master_hrms,
                "Employee": employee_hrms,
                "Management" :management_hrms,
                "Authorisation" :authorisation_hrms,
                "Training" :training_hrms
            })
     
    return dictionay_of_db_with_module

                
                                                           
def search_in_the_database_module_to_page_table(key_word):
    dictionay_of_db_with_module = categroise_table_as_module()

    for module, sub_dict in dictionay_of_db_with_module.items():
        if not isinstance(sub_dict, dict):
            continue

        for category, tables in sub_dict.items():
            if not isinstance(tables, list):
                continue

            for table in tables:
                result = to_get_the_value_from_df(key_word, table)

                if result is not None and not result.empty:
                    print("Module :", module)
                    print("Category :", category)
                    print(f"Found in table : {table}")
                    print(f"Result count  : {category}[{len(result)}]")
                    print(result)

    




