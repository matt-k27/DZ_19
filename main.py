import string

print('DZ19')

def is_palindrome(text):
    tempData = ''
    for symbol in text.lower():
        if not (symbol in string.punctuation) and symbol != ' ':
            tempData += symbol

    if tempData == tempData[::-1]:
        return True
    else:
        return False


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")

print('Thank you for using')
