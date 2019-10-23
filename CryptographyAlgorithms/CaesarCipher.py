def encryption(str1,key):
    str2=''
    for i in str1:
        if i.islower():
            str2+=chr((((ord(i)-97)+key)%26)+97)
        if i.isupper():
            str2+=chr((((ord(i)-65)+key)%26)+65)
    return str2

def decryption(str1,key):
    str2=''
    for i in str1:
        if i.islower():
            str2+=chr((((ord(i)-97)-key)%26)+97)
        if i.isupper():
            str2+=chr((((ord(i)-65)-key)%26)+65)
    return str2

    str1=input() /*message to be sent*/
    key=int(input()) /*key to be shared among sender and receiver*/
    str2=encryption(str1,key)
    print(str2) /*encypted text*/
    str2=decryption(str2,key)
    print(str2) /*decypted or original text*/
