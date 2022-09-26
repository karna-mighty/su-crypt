import colorama as c
from colorama import Fore, Back, Style

c.init(autoreset=True)

print(Fore.RED  + Style.BRIGHT  + """
                                                          _   
 ___      _   _              ___   _ __   _   _   _ __   | |_ 
/ __|    | | | |    _____   / __| | '__| | | | | | '_ \  | __|
\__ \    | |_| |   |_____| | (__  | |    | |_| | | |_) | | |_ 
|___/uper \__,_|ser         \___| |_|     \__, | | .__/   \__|
                                          |___/  |_|          
                                                          """)


def encrypt():
    text=input("enter the text to encrypt\n")
    key=input("enter your key to protect \n")

    dec = 0
    for i in key:
        dec+=ord(i)


    a=[]
    b=[]
    dec=dec//26

    for i in range(32,127):
        a.append(str(chr(i)))
        
    
    for i in range(len(text)):
        for j in range(len(a)):
            if (text[i]==a[j]):
                b.append(j-dec)

    for i in b:
        print(a[i],end="")
        

def decrypt():
    
    text=input("enter your encrypted text\n")
    key=input("enter your key \n")
    dec = 0
    for i in key:
        dec+=ord(i)
   


    a=[]
    b=[]

    crypt=[]

    dec=dec//26

    for i in range(32,127):
        a.append(str(chr(i)))
    

    for i in range(len(text)):
        for j in range(len(a)):
            if (text[i]==a[j]):
       
                b.append(j)
    

    for i in b:
    
    
        if i+dec < len(a):
    	    crypt.append(a[i+dec])
    	
        else:
    	    crypt.append(a[(i+dec)-95])
    	    
    for i in crypt:
        print(i,end="")
    	  
