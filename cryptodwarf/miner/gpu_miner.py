

class GpuMiner(object):

    def __init__(self, id, speed, accepted_shares, rejected_shares, *args, **kwargs):
        self._id = id
        self._speed = speed
        self._accepted_shares = accepted_shares
        self._rejected_shares = rejected_shares
        self._data = {
            'id': id,
            'speed': speed,
            'accepted_shares': accepted_shares,
            'rejected_shares': rejected_shares
        }

    @property
    def speed(self):
        return self._speed

    @property
    def id(self):
        return self._id

    @property
    def accepted_shares(self):
        return self._accepted_shares

    @property
    def rejected_shares(self):
        return self._rejected_shares

    @property
    def data(self):
        return self._data


class GpuMinerCollection(object):

    def __init__(self, *args, **kwargs):
        self.gpu_miners = []

    def add_gpu_miner(self, gpu_miner):
        self.gpu_miners.append(gpu_miner)

    def __iter__(self):
        return iter(self.gpu_miners)

    def calculate_data(self):
        self._total_speed = 0
        self._total_accepted_shares = 0
        self._total_rejected_shares = 0
        for gpu_miner in self:
            self._total_speed += gpu_miner.speed
            self._total_accepted_shares += gpu_miner.accepted_shares
            self._total_rejected_shares += gpu_miner.rejected_shares

    @property
    def total_speed(self):
        return self._total_speed

    @property
    def total_accepted_shares(self):
        return self._total_accepted_shares

    @property
    def total_rejected_shares(self):
        return self._total_rejected_shares

    @property
    def data(self):
        self.calculate_data()
        data = {
            'total_speed': self.total_speed,
            'total_accepted_shares': self.total_accepted_shares,
            'total_rejected_shares': self.total_rejected_shares,
            'gpu': []
        }
        for gpu_miner in self:
            data['gpu'].append(gpu_miner.data)
        return data
