from datetime import datetime
import pprint

class BaseMiner(object):

    def __init__(self, *args, **kwargs):
        pass

    def start(self, *args, **kwargs):
        self.started_time = datetime.now()

    def refresh(self):
        raise NotImplementedError('Implement refresh function')

    @property
    def miner_name(self):
        return self.MINER_NAME

    @property
    def coin_name(self):
        return self._coin_name

    def running_time(self):
        return datetime.now() - self.started_time

    def populate_gpu_miner(self):
        raise NotImplementedError('Implement populate_gpu_miner function')

    @property
    def data(self):
        raise NotImplementedError('Implement class property data')

    def print(self):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.data)
