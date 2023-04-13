import sys
import os
cmd="apt update && apt install wkhtmltopdf"
os.system(cmd)
import pdfkit
url=input("enter the url:>>>")
print("or")
file=input("input file to convert to html:>>>")
print("or")
string=input("enter html string to convert to pdf:>>>")
# directly from url
def from_url():
  pdfkit.from_url(url, url.pdf, verbose=True)
print("="*50)
# from file
def from_file():
  pdfkit.from_file(file, "index.pdf", verbose=True, options={"enable-local-file-access": True})
print("="*50)
# from HTML content
def from_html():
  pdfkit.from_string(string, "string.pdf", verbose=True)
print("="*50)
#hackertools by iyanuhacks
#thanks for using this tool
