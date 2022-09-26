import maincode as mc
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

ch=int(input("1 for encryption and 2 for decryption"))
if ch==1:
  mc.encrypt()
elif ch==2:
  mc.decrypt()
else:
  print("enter only 1 and 2 no other elements")
