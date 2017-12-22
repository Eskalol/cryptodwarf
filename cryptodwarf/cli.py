import fire
from cryptodwarf.machine.gpu import GPUCollection
from cryptodwarf.miner.miners.ewbf import ZcashEwbf
from cryptodwarf.miner.miner_collection import MinerCollection

class CryptoDwarf(object):

	def __int__(self, config_file='', verbose=False):
		pass

	def start(self):
		while True:
			gpus = GPUCollection()
			gpus.refresh()
			gpus.print()

			miners = MinerCollection()
			miners.add_miner(ZcashEwbf(42000))
			miners.refresh()
			miners.print()
			input("ENTER FOR next stats")

if __name__ == '__main__':
	fire.Fire(CryptoDwarf)
