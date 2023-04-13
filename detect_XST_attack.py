#code by Iyanuhacks
#hackertools
import requests
#After importing the requests library, create an array of HTTP methods, which we are going to send. We will make use of some standard methods like 'GET', 'POST', 'PUT', 'DELETE', 'OPTIONS' and a non-standard method ‘TEST’ to check how a web server can handle the unexpected input.

method_list = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'TRACE','TEST']
#The following line of code is the main loop of the script, which will send the HTTP packets to the web server and print the method and the status code.

for method in method_list:
   req = requests.request(method, 'Enter the URL')
   print(method, req.status_code, req.reason)
#The next line will test for the possibility of cross site tracing (XST) by sending the TRACE method.

if method == 'TRACE' and 'TRACE / HTTP/1.1' in req.text:
   print ('Cross Site Tracing(XST) is possible')
