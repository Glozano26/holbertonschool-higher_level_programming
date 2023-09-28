#!/usr/bin/python3
def uppercase(str):
    let2 = ""
    for letters in str:
        if 'a' <= letters and letters <= 'z':
            lett_upper = chr(ord(letters) - ord('a') + ord('A'))
            let2 += lett_upper
        else:
            let2 += letters
    return letters
