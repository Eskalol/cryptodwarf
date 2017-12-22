

class MinerCollection(object):

	def __init__(self, *args, **kwargs):
		self.miners = []

	def add_miner(self, miner):
		self.miners.append(miner)

	def __iter__(self):
		return iter(self.miners)

