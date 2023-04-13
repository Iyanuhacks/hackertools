"""code by Iyanuhacks"""
#hackertools
import mechanize
#Now, provide the name of the URL for obtaining the response after submitting the form.

url = input("Enter the full url:>>>")
attack_no = input("enter attack number:>>>")
#We need to read the attack vectors from the file.

with open('vectors_XSS.txt','r') as x:
  #Now we will send request with each arrack vector −

 for line in x:
   browser.open(url)
   browser.select_form(nr = 0)
   browser["id"] = line
   res = browser.submit()
content = res.read()
#The following line of code will check the printed attack vector.

if content.find(line) > 0:
  print("Possible XSS")
"""The following line of code will write the response to output file."""

output = open('response/' + str(attack_no) + '.txt', 'w')
output.write(content)
output.close()
print(attack_no)
attack_no += 1
