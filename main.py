import os, json, requests, webbrowser, time
from libs import *

def main():

    def_dir = os.getcwd()

    while True:
        clear()
        os.chdir(def_dir)
        option = ""
        while True:
            option = input("Welcome to the MC-Server-Manager! Pick your option\n1 - Create new server\n2 - Launch existing server\n3 - exit\n>>> ")
            if option == "1" or option == "2" or option == "3" or option == "exit":
                break
        if option == "1":

            links = import_links()

            version_input = input("What version do you want to download?\nBy downloading, you agree to Minecraft EULA, as it will be auto-filled. Get info about it by writing EULA: \n>>> ")

            if "eula" in version_input.lower():
                webbrowser.open("https://account.mojang.com/documents/minecraft_eula")
            elif version_input in links:
                if "servers" not in os.listdir():
                    os.mkdir("servers")
                os.chdir("servers")

                if version_input in os.listdir():
                    versions = 0
                    for i in os.listdir():
                        if version_input in i:
                            versions += 1
                    os.mkdir("%s-%d" % (version_input, versions))
                    os.chdir("%s-%d" % (version_input, versions))
                else:
                    os.mkdir("%s" % version_input)
                    os.chdir("%s" % version_input)

                download_file(links[version_input])

                memory = int(input("How much memory do you want your server to have? (specify in MB) > "))

                with open("eula.txt", "w+") as f:
                    f.write("eula=true")

                flags = yesorno("Do you want to enable --nogui flag? Y/n > ")
                clear()
                if flags == True:
                    os.system("java -Xms%dM -Xmx%dM -jar server.jar --nogui" % (memory, memory))
                else:
                    os.system("java -Xms%dM -Xmx%dM -jar server.jar" % (memory, memory))
        if option == "2":
            os.chdir("servers")
            if len(os.listdir()) != 0:
                servers = 1
                server_list = []
                for i in os.listdir():
                    print("%d - %s" % (servers, i))
                    servers += 1
                    server_list.append(i)
                server_input = input("Select which server do you want to start > ")
                os.chdir(server_list[int(server_input) - 1])

                memory = int(input("How much memory do you want your server to have? (specify in MB) > "))
                flags = yesorno("Do you want to enable --nogui flag? Y/n > ")
                clear()
                if flags == True:
                    os.system("java -Xms%dM -Xmx%dM -jar server.jar --nogui" % (memory, memory))
                else:
                    os.system("java -Xms%dM -Xmx%dM -jar server.jar" % (memory, memory))
            else:
                print("You haven't created a server yet!")
        if option == "3" or option == "exit":
            break


if __name__ == "__main__":
    main()





