import httpx

class Requests:
    def __init__(self, 
                url: str,
                headers=None,
                data=None,
                params=None):
        self.url = url
        self.head = headers
        self.data = data
        self.params = params

    async def get(self):
        try:
            async with httpx.AsyncClient() as client:
                requests = await client.get(url=self.url, headers=self.head, params=self.params)

                return requests

        except httpx.HTTPError:
            return()

    async def post(self):
        try:
            async with httpx.AsyncClient() as client:
                requests = await client.post(url=self.url, data=self.data, headers=self.head, params=self.params)

                return requests

        except httpx.HTTPError:
            return()