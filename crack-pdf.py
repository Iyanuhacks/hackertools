from banner import banner3
print(banner)
import pikepdf
from tqdm import tqdm
targetpdf=input("input targets pdf-file:>>>")
# load password list
passwords = [ line.strip() for line in open("wordlist.txt") ]

# iterate over passwords
for password in tqdm(passwords, "Decrypting PDF"):
    try:
        # open PDF file
        with pikepdf.open("foo-"targetpdf, password=password) as pdf:
            # Password decrypted successfully, break out of the loop
            print("[+] Password found:", password)
            break
    except pikepdf._qpdf.PasswordError as e:
        # wrong password, just continue in the loop
        continue
#hackertools by iyanuhacks
#thanks for using this tool
