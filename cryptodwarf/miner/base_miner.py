import datetime

class BaseMiner(object):
	
	MINER_NAME = ''

	def __init__(self, *args, **kwargs):
		pass

	def start(self, **args, **kwargs):
		self.started_time = datetime.now()

	@property
	def total_hashrate(self):
		raise NotImplementedError('Implement total_hashrate function.');

	@property
	def hash_rate_for_each_gpu(self):
		raise NotImplementedError('Implement hash_rate_for_each_gpu function.')

	@property
	def miner_name(self):
		return self.MINER_NAME

	@property
	def pool(self):
		return self._pool

	def running_time(self):
		return datetime.now() - self.started_time
