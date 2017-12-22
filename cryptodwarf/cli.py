import fire
from cryptodwarf.machine.gpu import GPUCollection


class CryptoDwarf(object):

	def __int__(self, config_file='', verbose=False):
		pass

	def start(self):
		while True:
			gpus = GPUCollection()
			gpus.refresh()
			gpus.print()
			input("ENTER FOR next stats")

if __name__ == '__main__':
	fire.Fire(CryptoDwarf)
