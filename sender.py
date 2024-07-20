# i will complet the code tomorrow i'm tires
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
     userfirstchoice = int(input('[+] Your choice: '))
     if userfirstchoice == 1:
         print('[+] Creating room...')
         roomcreationrequest=requests.post(url=f'{url}/createroom.php')
         roomcreationrequestresposnejsonformat=json.loads(roomcreationrequest.text)
         if roomcreationrequestresposnejsonformat['success'] == 'true':
             print(f'[+] Room created successfully | ID = {roomcreationrequestresposnejsonformat['roomId']}')

         if roomcreationrequestresposnejsonformat['success'] == 'false':
             print(f'[X] Error, Failed to create room')
     if userfirstchoice == 2:
         roomlisteninguserchoice = input('[X] RoomId : ')
     if userfirstchoice ==3:
         while True:
             sendmessageroomidinput = input('[+] roomId : ')
             if sendmessageroomidinput is None:
                 print('[X] Username cannot be empty')
             else:
                 while True:
                     usernames = ['Robert','James','John','Michael','William','David','Richard','Charles','Joseph' ,'Thomas','Christopher','Daniel','Paul','Mark','Donald','George']
                     username = random.choice(usernames)
                     stmessage = input('[+] \n\n[+] Your message: ')
                     stmessage = f'{username} : {stmessage}'
                     stmessagerequest = requests.post(url = f'{url}/sendmessage.php',data=f'roomid={sendmessageroomidinput}&message={stmessage}')                                print(stmessagerequest.text)
