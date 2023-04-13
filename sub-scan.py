import os
from colorama import init
###script by iyanuhacks###

"""
name    -----iyanuhacks---

github  ------https://github.com/iyanuhacks

WhatsApp -----+2347040435636

give me a star ⭐ if you copied this code

"""

cmd = 'clear'
os.system(cmd)
info="""
【s】【u】【b】【-】【s】【c】【a】【n】

          by iyanuhacks
######################################
____________________________________ 
name      | -----iyanuhacks---
__________|______________________
github    |------https://github.com/iyanuhacks
__________|_______________________
WhatsApp  |-----+2347040435646           
__________|____________________________

give me a star ⭐ if you like this tool
[+]this script can be used for finding a subdomain of any urls with over 1000 subdomain files

######################################
"""


print(info)
# the domain to scan for subdomains

import requests
  
# function for scanning subdomains
def domain_scanner(domain_name,sub_domnames):
    print('----URL after scanning subdomains----')
      
    # loop for getting URL's
    for subdomain in sub_domnames:
        
        # making url by putting subdomain one by one
        url = f"https://{subdomain}.{domain_name}"
          
        # using try catch block to avoid crash of the
        # program
        try:
            # sending get request to the url
            requests.get(url)
              
            # if after putting subdomain one by one url 
            # is valid then printing the url
            print(f'[+] {url}')
              
            # if url is invalid then pass it
        except requests.ConnectionError:
            pass
  
# main function
if __name__ == '__main__':
    
    # inputting the domain name
    dom_name = input("Enter the Domain Name:")
  
    # opening the subdomain text file
    with open('subdomains.txt','r') as file:
        
        # reading the file
        name = file.read()
          
        # using spilitlines() function storing the list
        # of splitted strings
        sub_dom = name.splitlines()
          
    # calling the function for scanning the subdomains
    # and getting the url
    domain_scanner(dom_name,sub_dom)
     
