import logging
from aiohttp import ClientRequest, ClientResponse


logger = logging.getLogger(__name__)
logging.basicConfig(
    format='[%(asctime)s] <%(levelname)s>  %(message)s',
    level=logging.INFO
)

class RequestClass(ClientRequest):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logging.info("|  send  |[%s]", self.url)


class ResponseClass(ClientResponse):
    async def start(self, connection):
        resp = await super().start(connection)
        logging.info("|response|[%s] (status)[%d]", self.url, self.status)
        return resp
