#!/usr/bin/env python3
import os
def main():
    print(''' _________  ____   ___   ___  _____ 
|__  / ___||  _ \ / _ \ / _ \|  ___|
  / /\___ \| |_) | | | | | | | |_   
 / /_ ___) |  __/| |_| | |_| |  _|  
/____|____/|_|    \___/ \___/|_|    ''')
    print("\n\nTool developed by zereza\n\n")
    username = "USERNAME FROM SENDINBLUE HERE"
    password = "PASSWORD FROM SENDINBLUE HERE"
    target = input("The target's email  ---->    ")
    name = input("\n\nThe target's name [OPTIONAL]  ---->   ")
    sender = input("\n\nThe sender of the email   ---->   ")
    subject = input("\n\nThe email subject  ---->   ")
    message = input("\n\nThe email message  ---->   ")
    
    if name == '':
        os.system('sendemail -xu '+username+' -xp '+password+' -f '+sender+' -t '+target+' -u '+subject+' -m '+message+' -s "smtp-relay.sendinblue.com:587"')
    else:
        os.system('sendemail -xu '+username+' -xp '+password+' -f '+sender+' -t '+target+' -u '+subject+' -m '+message+' -s "smtp-relay.sendinblue.com:587" -o message-header="From '+name+'<'+sender+'>"')
    
if __name__ == '__main__':
    main()
