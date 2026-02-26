from app.data_base_collection import *
dictionay_of_db_with_module = {
    "Admission": {},
    "Preadmission": {"Marks": "", "Master": "","Caste":"","Fees_Payment":""},
    "Fees": {},
    "Exam": {},
    "Inventory": {},
    "HRMS": {}
}

def categroise_table_as_module():
    for key, val in dict_of_all_modules.items():

        if key == "Preadmission_":
            marks = [i for i in val if "Marks" in i]
            master = [j for j in val if "Master" in j]
            caste = [k for k in val if "caste" in k]
            fees_pay = [l for l in val if "Fee_" in l]

            dictionay_of_db_with_module["Preadmission"].update({
                "Marks": marks,
                "Master": master,
                "Caste" :caste,
                "Fees_Payment" :fees_pay
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

    




