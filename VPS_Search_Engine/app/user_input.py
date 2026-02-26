from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from app.search_text import from_key_board
from app.data_base_collection import *
from app.word_comp import word_completor
from app.anylng_to_eng import *
from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion
import unicodedata
from googletrans import Translator
from langdetect import detect
import unicodedata
from app.data_base_collection import *
translator = Translator()


def translate_to_english_if_needed(text: str) -> str:
    try:
        # Normalize Unicode (FIX)
        text = unicodedata.normalize("NFC", text)

        lang = detect(text)
        if lang != "en":
            translated = translator.translate(text, dest="en").text
            print(f"[Translated '{text}' → '{translated}']")
            return translated
        return text

    except Exception as e:
        print("Translation skipped:", e)
        return text
    

def load_db_data(DATA_DB):
    with open(DATA_DB, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]
    
class DBLimitedCompleter(Completer):
    def __init__(self, data, max_items=6):
        self.data = data
        self.max_items = max_items

    def get_completions(self, document, complete_event):
        text = document.text.strip()

        if not text:
            return

        count = 0  # 🔒 hard limit

        for item in self.data:
            # convert DB value to string safely
            item_str = str(item)

            if item_str.startswith(text):
                yield Completion(
                    item_str,
                    start_position=-len(text)
                )
                count += 1

                if count == self.max_items:
                    break   # ✅ STOP at 6

UPDATED_DATA_DB = load_db_data(DATA_DB)
sub_Module =""
def to_return_choice(your_input,module_text):
    if your_input == 1:

        # -------------------------------
        # STEP 1: First raw input
        # -------------------------------
        raw_input = prompt("Type word (any language): ")
        text = unicodedata.normalize("NFC", raw_input)

        # -------------------------------
        # STEP 2: Language detection
        # -------------------------------
        try:
            lang = detect(text)
        except:
            lang = "unknown"

        # -------------------------------
        # STEP 3: Translate if NOT English
        # -------------------------------
        if lang != "en":
            text = translate_to_english_if_needed(text)
            print(f"Converted (English): {text.title()}")

        # -------------------------------
        # STEP 4: SINGLE autocomplete path
        # -------------------------------
        completer = DBLimitedCompleter(UPDATED_DATA_DB, max_items=6)

        final_value = prompt(
            "Select from suggestions: ",
            completer=completer,
            default=text.title()
        )

        print("Selected:", final_value)
        sub_Module  = final_value
    elif your_input == 2:
        sub_Module = live_speech_to_english()
        print(f"Converted (English): {sub_Module.title()}")
        sub_Module = sub_Module.title()
    return sub_Module  

def to_choose_module(module_name):
    if module_name == "Preadmission":
        from_key_board(PREADMISSION_MODULE_KEWORDS,module_name)
    elif module_name == "Admission" or module_name == "Entry":
        from_key_board(ADMISSION_MODULE_KEWORDS,module_name)
    elif module_name == "Fees" or module_name =="Charges":
        from_key_board(FEES_MODULE_KEYWORDS,module_name)
    elif module_name == "Exam":
        from_key_board(EXAM_MODULE_KEYWORDS,module_name)
    elif module_name == "HRMS":
        from_key_board(HRMS_MODULE_KEYWORDS,module_name)
    elif module_name == "Inventory":
        from_key_board(INVENTORY_MODULE_KEYWORDS,module_name)
    else:
        pass