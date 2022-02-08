#!/usr/bin/env python3
import os
import sys
import requests
import time

#warna
red = '\033[91m'
green = '\033[92m'
white = '\033[00m'

#animasi
def load_animation():    
    load_str = "i am not a hacker i am just tester..."
    ls_len = len(load_str) 
    animation = "|/-\\"
    anicount = 0
    counttime = 0        
    i = 0                     
    
    while (counttime != 100): 
        time.sleep(0.075)  
        load_str_list = list(load_str)
        x = ord(load_str_list[i]) 
        y = 0                             
        if x != 32 and x != 46:              
            if x>90: 
                y = x-32
            else: 
                y = x + 32
            load_str_list[i]= chr(y) 
        res =''              

        for j in range(ls_len): 

            res = res + load_str_list[j] 
        sys.stdout.write("\r"+res + animation[anicount]) 
        sys.stdout.flush() 
        load_str = res 
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len 
        counttime = counttime + 1

# windows
    if os.name =="nt": 
        os.system("cls") 
# linux / Mac OS 
    else:
        os.system("clear") 
if __name__ == '__main__':  
    load_animation()
    

logo = '''

           1010010        0001101
           1000100        0011100
           0110011        1001001
           1011001        0010111
           1010100        0100100
           1110010101011100010100
           101010000HADES01011100
           1010101000111000100001
           0011100        1000000
           1001000        0100100
           1010101        1000110
           1100110        0011100
           1010001        0011111


 [-] I AM NOT HACKER, I AM JUST TESTER[-]


'''

print (red+logo+white)

#inputan
def main():
    print("\033[34m[*] \033[0mTarget Url http://contoh.com")
    target = input("Enter Target Url: ")
    url = target

    #animasi
    start = "Start Scanning...\n"
    for s in start:
        sys.stdout.write(s)
        sys.stdout.flush()
        time.sleep(0.1)
    
    #open file
    file = open("admin.txt", "r")	
    try:
        for link in file.read().splitlines():
            curl = url + link
            res = requests.get(curl)
            if res.status_code == 200:
                print("*" * 20)
                print("\033[32mKetemu boyyy --> {} \033[0m".format(curl))
                print("*" * 20)
            else:
                print("\033[91m[-] G ada --> {} \033[0m".format(curl))
    
    except KeyboardInterrupt:
        print("\033[91mMematikan program ! \033[0m")
    except:
        print("\033[91mError g di ketahui ! \033[0m")
    
    file.close()

if __name__ == "__main__":
    main()
