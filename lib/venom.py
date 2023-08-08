import cv2, os, random
from .text import italic, BLACK, WHITE, CYAN
from .requests import Requests
from .agents import user_agent
from .objects import TempPrint

"""
Venom is a facial recognition feature used by Eyes when working with the GitHub module.

How does it work ?
    - Venom uses cv2 module to recognize faces on GitHub profile picture

Tasks:
    - upload of the github profile picture
    - find or not the faces
    - create a .jpg file with red squares around the faces
    - delete the entry profile picture
"""

class Face:

    async def uploader(url, name: str):
        PATH = "facial_recognition/{}.jpg".format(name)

        headers = {
            'user-agent': random.choice(user_agent())
        }

        req = await Requests(url, headers).get()

        TempPrint(BLACK+"[+] Upload of profile picture..."+WHITE).Tprint()
        with open(PATH, 'wb') as file:
                            file.write(req.content)

        return PATH


    async def facial(url, name: str, output_path):
        input_path = await Face.uploader(url, name)

        f_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        image = cv2.imread(input_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        detect = f_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        if len(detect) > 0:
            print(italic("[VENOM] 🎭 Face detected !\n"))

            for (x, y, w, h) in detect:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)

            cv2.imwrite(output_path, image)

            TempPrint(BLACK+"[+] Profile picture removal..."+WHITE).Tprint()
            os.remove(input_path)
            file_path = os.path.abspath(output_path)
            print(italic(f"{BLACK}[+] Result save here : {CYAN}{file_path}{WHITE}\n"))

        else:
            TempPrint("[+] Profile picture removal...").Tprint()
            os.remove(input_path)
            pass