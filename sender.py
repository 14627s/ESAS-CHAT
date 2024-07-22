import base64
import requests
import time
import os
import json
import random

url = 'https://e2echat.000webhostapp.com/'

def clear(): 


    if os.name=='nt': 
        os.system('cls')
    else: 
        os.system('clear')


def first():
    while True:
     clear()
     print('    --- ESAS CHAT SENDER ---   \n\n')
     username = input("[+] Your username: ")
     if username is None:
         print('[X] Username cannot be empty')
     else:
         break

def choices():
    print('[1] Create a room\n[2] Listen in a room\n[3] Start sending messages')
    while True:
     userfirstchoice = int(input('\n[+] Your choice: '))
     if userfirstchoice == 1:
         print('[+] Creating room...')
         roomcreationrequest=requests.post(url=f'{url}/createroom.php')
         roomcreationrequestresposnejsonformat=json.loads(roomcreationrequest.text)
         if 'error' in (roomcreationrequest.text):
             print(f'[X] Error, Failed to create room')
         else:
             print(f'[+] Room created successfully | ID = {roomcreationrequestresposnejsonformat['roomId']}')

     if userfirstchoice == 2:
         roomlisteninguserchoice = input('[X] RoomId : ')
     if userfirstchoice ==3:
         while True:
             sendmessageroomidinput = input('[+] roomId : ')
             if sendmessageroomidinput is None:
                 print('[X] RoomId cannot be empty')
             else:
                 usernames = ['Robert', 'James', 'John', 'Michael', 'William', 'David', 'Richard', 'Charles', 'Joseph',
                              'Thomas', 'Christopher', 'Daniel', 'Paul', 'Mark', 'Donald', 'George']
                 username = random.choice(usernames)
                 while True:

                     stmessage = input('\n[+] Your message: ')
                     toencodedmessage=(f'{username}: {stmessage}').encode('utf-8')
                     encode0dmessage=base64.b64encode(toencodedmessage)
                     data = {
                         'roomid': sendmessageroomidinput,
                         'message': encode0dmessage.decode('utf-8')
                     }
                     stmessagerequest = requests.post(url = f'{url}/sendmessage.php', data=data)
choices()
