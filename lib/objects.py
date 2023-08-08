import time

class TempPrint:
    def __init__(self,
                text: str,
                time: int=3) -> None:
        self.text = text.rstrip()
        self.time = time

    def Tprint(self):
        print(self.text, end="", flush=True)
        time.sleep(self.time)
        print("\r" + " " * (len(self.text) + 1) + "\r", end="", flush=True) # clear text printer