# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 22:25:59 2021

"So'z topish" o'yini

@author: user
"""
import random
from uzwords import words
from transliterate import to_latin

def get_words():
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return to_latin(word).upper()


def display(user_letters,word):
    display_letters = ""
    for letter in word:
        if letter in user_letters.upper():
            display_letters += letter
        else:
            display_letters += "-"
    return display_letters


def play():
    word = get_words()
    word_letters = set(word)
    user_letters = ''
    print(f"Men {len(word)} xonali so'z o'yladim. Topa olasizmi ?")
    while len(word_letters)>0:
        print(display(user_letters,word))
        if len(user_letters)>0:
            print(f"Shu vaqtgacha kiritgan harflaringiz: {user_letters}")
            
        letter = input("Harf kiriting: ").upper()
        if letter in user_letters:
            print("Bu harfni avval kiritgansiz. Boshqa harf kiriting.")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} harfi to'g'ri")
        else:
            print("Bunday harf yo'q")
        user_letters += letter
    print(f"Tabriklayman! {word} so'zini {len(user_letters)} ta urinish bilan topdingiz")
    
        
        
        
        
        
        
    