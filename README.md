# Pico-Ducky-Stuff
Scripts and some other stuff used to create, manage and use a Raspberry Pico as Ducky USB

### *Reverse TCP connection*

## How does this reverse tcp connection work?
- A Raspberry Pico, which was modified, is plugged into a victim pc
- The Ducky script initiates itself and opens powershell
- Powershell then downloads another payload (the tcp client) and runs it
- (Not tested yet) The program should directly run in powershell, this means that the actual file never touches the victims pc
- ^ This should also prevent windows AV of noticing smth odd
