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
    
    text=input("enter your encrypoted text\n")
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
    	  
