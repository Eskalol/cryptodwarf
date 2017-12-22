from gpustat import new_query
import pprint

class GPU(object):

	def __init__(self, entry, *args, **kwargs):
		self.entry = entry

	def __getitem__(self, key):
		return self.entry[key]

	def get_all(self):
		return self.entry

	def keys(self):
		return self.entry.keys()

	@property
	def name(self):
		"""
        Returns the name of GPU card (e.g. Geforce Titan X)
        """
		return self.entry['name']

	@property
	def index(self):
		"""
        Returns the index of GPU (as in nvidia-smi).
        """
		return self.entry['index']

	@property
	def temperature(self):
		"""
        Returns the temperature of GPU as an integer,
        or None if the information is not available.
        """
		v = self.entry['temperature.gpu']
		return int(v) if v is not None else None

	@property
	def utilization(self):
		"""
        Returns the GPU utilization (in percentile),
        or None if the information is not available.
        """
		v = self.entry['utilization.gpu']
		return int(v) if v is not None else None

	@property
	def memory_total(self):
		"""
        Returns the total memory (in MB) as an integer.
        """
		return int(self.entry['memory.total'])

	@property
	def memory_used(self):
		"""
        Returns the occupied memory (in MB) as an integer.
        """
		return int(self.entry['memory.used'])

	@property
	def memory_free(self):
		"""
        Returns the free (available) memory (in MB) as an integer.
        """
		v = self.memory_total - self.memory_used
		return max(v, 0)

	@property
	def power_draw(self):
		"""
        Returns the GPU power usage in Watts,
        or None if the information is not available.
        """
		v = self.entry['power.draw']
		return int(v) if v is not None else None

	@property
	def power_limit(self):
		"""
        Returns the (enforced) GPU power limit in Watts,
        or None if the information is not available.
        """
		v = self.entry['enforced.power.limit']
		return int(v) if v is not None else None

class GPUCollection(object):

	def __init__(self, *args, **kwargs):
		self.gpus = []

	def add_gpu(self, gpu):
		self.gpus.append(gpu)

	def __iter__(self):
		return iter(self.gpus)

	def add_nvidia_gpus(self):
		for gpu in new_query():
			self.add_gpu(self.create_nvidia_gpu(gpu))

	def create_nvidia_gpu(self, gpu):
		kwargs = {}
		kwargs['memory.used'] = gpu.memory_used
		kwargs['memory.total'] = gpu.memory_total
		kwargs['utilization.gpu'] = gpu.utilization
		kwargs['temperature.gpu'] = gpu.temperature
		kwargs['index'] = gpu.index
		kwargs['name'] = gpu.name
		kwargs['power_draw'] = gpu.power_draw
		kwargs['power_limit'] = gpu.power_limit
		return GPU(kwargs)

	def add_amd_gpus(self):
		pass

	def refresh(self):
		self.gpus = []
		self.add_nvidia_gpus()
		self.add_amd_gpus()

	def print(self):
		for gpu in self:
			pp = pprint.PrettyPrinter(indent=4)
			pp.pprint(gpu.get_all())
