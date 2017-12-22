from cryptodwarf.miner.base_miner import BaseMiner
from cryptodwarf.request.requests import Api
from cryptodwarf.request.exceptions import CryptoDwarfHttpError
import json
import pprint


class AbstractEwbf(BaseMiner):
    MINER_NAME = 'EWBF Miner'

    def __init__(self, port, *args, **kwargs):
        super(AbstractEwbf, self).__init__(*args, **kwargs)
        self.port = port

    def refresh(self):
        api = Api('http://127.0.0.1:{}/getstat'.format(self.port))
        try:
            response = api.get()
            self._data = json.dump(response)
        except CryptoDwarfHttpError as e:
            print(e) # TODO: logging

    def get_data(self):
        return self._data

    def print(self):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.get_data())


class ZcashEwbf(AbstractEwbf):

    def __init__(self, *args, **kwargs):
        super(ZcashEwbf, self).__init__(*args, **kwargs)
        self._coin_name = 'Zcash (ZEC)'
