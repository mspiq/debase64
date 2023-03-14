#!usr/bin/python
#By Mohamed Salah
#For Encode  Base64




from termcolor import colored
import base64
import time
print colored ('''
        +=======================================+
        |................Base64.................|
        +---------------------------------------+
        |............. Mohamed Salah ...........|
        +---------------------------------------+
: www.facebook.com/mspiq
''', 'red')

y=input("press input the hash:")


N=base64.b64decode(y)
print("please wait......")
time.sleep (5)
print ("Successfully decryption:\n"+(N))

printcolored ('''
           +========================================+
           |   Thank you can follow us on Facebook  |
           +========================================|
           |https://www.facebook.com/mspiq          |
           +========================================+
please Enter for Exit:''', 'red')
input(":")
