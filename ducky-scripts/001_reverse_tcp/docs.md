# *Reverse TCP connection*

## How does this reverse tcp connection work?
- A Raspberry Pico, which was modified, is plugged into a victim pc
- The Ducky script initiates itself and opens powershell
- Powershell then downloads another payload (the tcp client) and runs it
- (Not tested yet) The program should directly run in powershell, this means that the actual file never touches the victims pc
- ^ This should also prevent windows AV of noticing smth odd

## Some stuff that could be important when building python files to exe with pyInstaller
- USAGE: (pyInstaller should be in PATH): **pyinstaller --onefile --key 12345 "path\to\script.py"**
- add --noconsole and --nowindowed. When run payload will not be shown on the victims pc.
- for more info about pyInstaller follow this [link](https://pyinstaller.org/en/stable/usage.html).
