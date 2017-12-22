import fire
from cryptodwarf.machine.gpu import GPUCollection
from cryptodwarf.miner.miners.ewbf import ZcashEwbf


class CryptoDwarf(object):

	def __int__(self, config_file='', verbose=False):
		pass

	def start(self):
		while True:
			gpus = GPUCollection()
			gpus.refresh()
			gpus.print()
			zcash = ZcashEwbf(42000)
			zcash.refresh()
			zcash.print()
			input("ENTER FOR next stats")

if __name__ == '__main__':
	fire.Fire(CryptoDwarf)
