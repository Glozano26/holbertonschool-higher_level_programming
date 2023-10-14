#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """unction that prints a text with 2 new lines after each of
    these characters: ., ? and :
    """
    symbols = [".", "?", ":"]
    if is not isinstance(text, str):
        raise TypeError("text must be a string")
        result_esp = ""
    for char in text:
        if char == symbols:
            if char == " ":
                pass
            else:
                result_esp = ""
                print(char, end="")
                pass
        if char == symbols:
            print(char)
            print("")
            result_esp = char
        else:
            print(char, end="")
