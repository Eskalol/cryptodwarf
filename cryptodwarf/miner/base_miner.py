from datetime import datetime
import pprint

class BaseMiner(object):
    """
    BaseMiner class, this class should be inherited when
    new miner classes being created
    """
    def __init__(self, *args, **kwargs):
        pass

    def start(self, *args, **kwargs):
        self.started_time = datetime.now()

    def refresh(self):
        """
        Called whenever we update stats
        :return:
        """
        raise NotImplementedError('Implement refresh function')

    @property
    def data(self):
        """
        Should return stats data of the miner
        :return:
        """
        raise NotImplementedError('Implement class property data')

    @property
    def type(self):
        """
        nvidia or amd miner
        :return: string
        """
        return self._type

    @property
    def miner_name(self):
        """
        name of the miner
        :return: string
        """
        return self.MINER_NAME

    @property
    def coin_name(self):
        """
        returns the name of the coin
        Example:
            'zec' for Zcash
        :return:
        """
        return self._coin_name

    @property
    def coin_full_name(self):
        """
        Returns the full name of the coin
        Example:
            'Zcash (ZEC)' for zcash
        :return:
        """
        return self._coin_full_name

    def running_time(self):

        return datetime.now() - self.started_time

    def print(self):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.data)
