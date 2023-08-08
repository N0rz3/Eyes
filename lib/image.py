from PIL import Image
from io import BytesIO
import imagehash
from .requests import Requests 

async def fetch_img(url: str):
    req = await Requests(url).get()
    return Image.open(BytesIO(req.content))

def get_hashed(image: Image) -> str:
    return str(imagehash.average_hash(image))