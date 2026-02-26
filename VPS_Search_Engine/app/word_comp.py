from prompt_toolkit.completion import WordCompleter
def word_completor(key_with_module_name):
    with open(key_with_module_name, "r", encoding="utf-8") as f:
        words = [w.strip() for w in f]

    completer = WordCompleter(words, ignore_case=True)
    return completer