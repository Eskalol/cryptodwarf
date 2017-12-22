from cryptodwarf.miner.base_miner import BaseMiner
from cryptodwarf.request.requests import Api
from cryptodwarf.request.exceptions import CryptoDwarfHttpError
from cryptodwarf.miner.gpu_miner import GpuMiner, GpuMinerCollection


class AbstractEwbf(BaseMiner):
    MINER_NAME = 'EWBF Miner'

    def __init__(self, port, *args, **kwargs):
        super(AbstractEwbf, self).__init__(*args, **kwargs)
        self.port = port

    def refresh(self):
        api = Api('http://127.0.0.1:{}/getstat'.format(self.port))
        try:
            response = api.get()
            self._json = response.json()
            self.populate_gpu_miner()

        except CryptoDwarfHttpError as e:
            print(e) # TODO: logging

    def populate_gpu_miner(self):
        self.gpu_miner_collection = GpuMinerCollection()
        for gpu_miner in self._json['result']:
            self.gpu_miner_collection.add_gpu_miner(GpuMiner(
                gpu_miner['cudaid'],
                gpu_miner['speed_sps'],
                gpu_miner['accepted_shares'],
                gpu_miner['rejected_shares']
            ))

    @property
    def data(self):
        data = {
            'coin': self._coin_name,
            'miner': self.MINER_NAME
        }
        return {**data, **self.gpu_miner_collection.data}


class ZcashEwbf(AbstractEwbf):

    def __init__(self, *args, **kwargs):
        super(ZcashEwbf, self).__init__(*args, **kwargs)
        self._coin_name = 'Zcash (ZEC)'
