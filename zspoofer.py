#!/usr/bin/env python3
import os
from termcolor import colored
def main():
    print(colored(''' _________  ____   ___   ___  _____ 
|__  / ___||  _ \ / _ \ / _ \|  ___|
  / /\___ \| |_) | | | | | | | |_   
 / /_ ___) |  __/| |_| | |_| |  _|  
/____|____/|_|    \___/ \___/|_|    ''', 'red'))
    print(colored("\n\nTool developed by zereza\n\n", 'yellow', attrs=['bold']))
    username = "sterlingfreeman215@gmail.com"
    password = "6mskwXhRQfMK8JSB"
    target = input(colored("The target's email  ---->    ", 'green'))
    name = input(colored("\n\nThe sender's name [OPTIONAL]  ---->   ", 'green'))
    sender = input(colored("\n\nThe sender of the email   ---->   ", 'green'))
    subject = input(colored("\n\nThe email subject  ---->   ", 'green'))
    message = input(colored("\n\nThe email message  ---->   ", 'green'))
    
    if name == '':
        os.system('sendemail -xu \"'+username+'\" -xp \"'+password+'\" -f \"'+sender+'\" -t \"'+target+'\" -u \"'+subject+'\" -m \"'+message+'\" -s "smtp-relay.sendinblue.com:587" &>/dev/null')
        print(colored('Sent :)', 'yellow'))
    else:
        os.system('sendemail -xu \"'+username+'\" -xp \"'+password+'\" -f \"'+sender+'\" -t \"'+target+'\" -u \"'+subject+'\" -m \"'+message+'\" -s "smtp-relay.sendinblue.com:587" -o message-header="From: '+name+' <'+sender+'>" &>/dev/null')
        print(colored('Sent :)', 'yellow'))
    
if __name__ == '__main__':
    main()
