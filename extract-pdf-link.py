
import pikepdf # pip3 install pikepdf

file = input("file name:>>>")
# file = "choose file"
pdf_file = pikepdf.Pdf.open(file)
urls = []
# iterate over PDF pages
for page in pdf_file.pages:
    for annots in page.get("/Annots"):
        uri = annots.get("/A").get("/URI")
        if uri is not None:
            print("[+] URL Found:", uri)
chromosome            
urls.append(uri)

print("[*] Total URLs extracted:", len(urls))
#hackertools by iyanuhacks
#thanks for using this tool
