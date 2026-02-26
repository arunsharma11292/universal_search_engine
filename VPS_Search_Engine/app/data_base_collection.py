import pandas as pd
from sqlalchemy import create_engine
import urllib
from sqlalchemy import text
list_of_schema_table = []
list_of_pre_admision = []
list_of_admision = []
list_of_fees = []
list_of_HRMS = []
list_of_Exam = []
list_of_Inventory = []
dict_of_all_modules = {"Preadmission_":list_of_pre_admision,"Adm_":list_of_admision,"Fee":list_of_fees,"HR_":list_of_HRMS,"Exm_":list_of_Exam,"INV_":list_of_Inventory}
pree_add_all_values = []   # ONE final list


# Path of Module Name 
MODULE_NAME =r"D:\Project_with_Python\VPS_Search_Engine\modules_data\Module_List\module_text.txt"
#Path of Modules Keywords
ADMISSION_MODULE_KEWORDS = r"D:\Project_with_Python\VPS_Search_Engine\modules_data\Modules\Admisiion_module.txt"
PREADMISSION_MODULE_KEWORDS  = r"D:\Project_with_Python\VPS_Search_Engine\modules_data\Modules\Preadmission_module.txt"
FEES_MODULE_KEYWORDS = r"D:\Project_with_Python\VPS_Search_Engine\modules_data\Modules\Fees_module.txt"
EXAM_MODULE_KEYWORDS =r"D:\Project_with_Python\VPS_Search_Engine\modules_data\Modules\Exam_module.txt"
HRMS_MODULE_KEYWORDS = r"D:\Project_with_Python\VPS_Search_Engine\modules_data\Modules\HRMS_Module.txt"
INVENTORY_MODULE_KEYWORDS = r"D:\Project_with_Python\VPS_Search_Engine\modules_data\Modules\Inventory_Module.txt"
#Path of Module's DB
ADMISSION_DB = r"D:\Project_with_Python\VPS_Search_Engine\modules_data\Module_DB\Admission_DB.txt"
PREADMISSON_DB = r"D:\Project_with_Python\VPS_Search_Engine\modules_data\Module_DB\Preadmission_DB.txt"
FEES_DB =r"D:\Project_with_Python\VPS_Search_Engine\modules_data\Module_DB\Fees_DB.txt"
EXAM_DB = r"D:\Project_with_Python\VPS_Search_Engine\modules_data\Module_DB\Exam_DB.txt"
HRMS_DB =r"D:\Project_with_Python\VPS_Search_Engine\modules_data\Module_DB\HRMS_DB.txt"
INVENTORY_DB = r"D:\Project_with_Python\VPS_Search_Engine\modules_data\Module_DB\Preadmission_DB.txt"

DATA_DB = r"d:\Data_Science\Speech_to_text\Data_vps.txt"


def to_get_the_value_from_df(search_value,module):
    engine = to_connect_sql_server()
    df = pd.read_sql(f"SELECT * FROM {module}", engine)

    # search value in ANY column
    mask = (df.astype(str) == str(search_value)).any(axis=1)
    result = df[mask]

    # print only if value found
    if not result.empty:
        return(result)
def to_store_all_value_in_list(list_of_pre_admision):
    engine = to_connect_sql_server()
    for table in list_of_schema_table:
        if "Preadmission" in table:
            df = pd.read_sql(f"SELECT * FROM {table}", engine)
            for col in df.columns:
                pree_add_all_values.extend(df[col].dropna().tolist())
def to_get_list_of_module_items(module,list_for_module):
    for item in list_of_schema_table:
        if module in item:
            list_for_module.append(item)
        else:
              pass

def to_connect_sql_server(): 
    params = urllib.parse.quote_plus(
    "DRIVER={SQL Server};"
    "SERVER=ARUN_SHARMA\SQLEXPRESS01;"
    "DATABASE=NDA_Stag;"
    "Trusted_Connection=yes;")
    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
    return engine


def to_get_table_sch():
    
    engine = to_connect_sql_server()
    query = text("""
    SELECT TABLE_SCHEMA, TABLE_NAME
    FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_TYPE = 'BASE TABLE'
    """)

    with engine.connect() as conn:
        result = conn.execute(query)

        print("Tables in NDA_Stag :")
        for row in result:
            sch_tab = f"{row.TABLE_SCHEMA}.[{row.TABLE_NAME}]"
            list_of_schema_table.append(sch_tab)
