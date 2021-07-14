import json, requests, os

def import_links():
    with open("officialurl.json") as js:
        return(json.load(js))

def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open("server.jar", 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    return local_filename

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def yesorno(question):
    while True:
        answer = input(question)
        if answer.lower() == "y" or answer.lower() == "yes":
            return True
        elif answer.lower() == "n" or answer.lower() == "no":
            return False

