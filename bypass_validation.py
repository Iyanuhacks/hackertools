#hackertools by Iyanuhacks
import mechanize
#Now, we will create an object named brwsr of the mechanize browser −

brwsr = mechanize.Browser()
#The next line of code shows that the user agent is not a robot.

brwsr.set_handle_robots( False )
#Now, we need to provide the url of our dummy website containing the web form on which we need to bypass validation.

url = input("Enter URL:>>> ")
#Now, following lines will set some parenters to true.

brwsr.set_handle_equiv(True)
brwsr.set_handle_gzip(True)
brwsr.set_handle_redirect(True)
brwsr.set_handle_referer(True)
#Next it will open the web page and print the web form on that page.

brwsr.open(url)
for form in brwsr.forms():
   print(form)
#Next line of codes will bypass the validations on the given fields.

brwsr.select_form(nr = 0)
brwsr.form['name'] = ''
brwsr.form['gender'] = ''
brwsr.submit()
