"""
@FileName：case_lower_test.py
@Description：
@Author：shenxinyuan
@Time：2023/11/24
"""
string1 = "Hello"
string2 = "hello"

if string1.casefold() == string2.casefold():
    print("Strings are case-insensitive equal.")

string1 = "Hello"
string2 = "hello"

if string1.lower() == string2.lower():
    print("Strings are case-insensitive equal.")

string1 = "Hello"
string2 = "hello"

if string1.lower() == string2.lower():
    print("Strings are case-insensitive equal.")
