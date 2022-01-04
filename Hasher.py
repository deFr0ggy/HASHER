import sys
import hashlib
from colorama import *

def banner():

    gogo = '''

 __  __     ______     ______     __  __     ______     ______    
/\ \_\ \   /\  __ \   /\  ___\   /\ \_\ \   /\  ___\   /\  == \   
\ \  __ \  \ \  __ \  \ \___  \  \ \  __ \  \ \  __\   \ \  __<   
 \ \_\ \_\  \ \_\ \_\  \/\_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\ 
  \/_/\/_/   \/_/\/_/   \/_____/   \/_/\/_/   \/_____/   \/_/ /_/ v1.0
                                                                    
 An Automated Hash Calculator
 ------------------------------
 Coded by Kamran Saifullah - Frog Man
 Twitter: https://twitter.com/deFr0ggy 
 GitHub: https://github.com/deFr0ggy 
 LinkedIn: https://linkedin.com/in/kamransaifullah 

 Usage: ./Hasher.py <File>
    
    '''

    print(Fore.YELLOW + gogo)

def hashMe(sample):
    
    try:

        md5 = hashlib.md5()
        sha1 = hashlib.sha1()
        sha256 = hashlib.sha256()
        sha512 = hashlib.sha512()

        with open(sample, "rb") as file:
            EOF = 0
            while EOF != b'':
                EOF = file.read()
                md5.update(EOF)
                sha512.update(EOF)
                sha256.update(EOF)
                sha1.update(EOF)

        print(Fore.GREEN + "MD5: " + Fore.LIGHTMAGENTA_EX + md5.hexdigest())
        print(Fore.GREEN + "SHA1: " + Fore.LIGHTMAGENTA_EX + sha1.hexdigest())
        print(Fore.GREEN + "SHA256: " + Fore.LIGHTMAGENTA_EX + sha256.hexdigest())
        print(Fore.GREEN + "SHA512: " + Fore.LIGHTMAGENTA_EX + sha512.hexdigest())
        print(Fore.RESET)

    except:
        print("Nano!")

def main():

    banner()

    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("Invalid Arguments Provided!")
    else:
        hashMe(sys.argv[1])

if __name__ == '__main__':
    main()
    