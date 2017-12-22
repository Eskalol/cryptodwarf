import pprint


class MinerCollection(object):

	def __init__(self, *args, **kwargs):
		self.miners = []

	def add_miner(self, miner):
		self.miners.append(miner)

	def __iter__(self):
		return iter(self.miners)

	def refresh(self):
		for miner in self:
			miner.refresh()

	@property
	def data(self):
		return [ x.data for x in self ]

	def print(self):
		pp = pprint.PrettyPrinter(indent=4)
		pp.pprint(self.data)
