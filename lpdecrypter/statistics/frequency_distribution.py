import json

class FrequencyDistribution(object):
    """
        A class that represent a frequency distribution i.e. a map
         number - count
    """
    def __init__(self, name, entries={}, xlabel=None, ylabel=None):
        self.name = name
        self.entries = entries
        self.xlabel = xlabel
        self.ylabel = ylabel

    def write_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(json.dumps({
                'name': self.name,
                'entries': self.entries,
                'xlabel': self.xlabel,
                'ylabel': self.ylabel
            }))

    @staticmethod
    def from_file(filename):
        with open(filename, 'r') as f:
            data = json.loads(f.read())
        data['entries'] = {int(key): value for key, value in data['entries'].items()}
        return FrequencyDistribution(data['name'], entries=data['entries'], xlabel=data['xlabel'], ylabel=data['ylabel'])

    @staticmethod
    def from_list(list, name, entries={}, xlabel=None, ylabel=None):
        """
            Calculates the number of occurencies of each number in the list
        """
        frequencies = {}
        for value in list:
            if value in frequencies:
                frequencies[value] += 1
            else:
                frequencies[value] = 1
        distr = FrequencyDistribution(name, entries=frequencies, xlabel=xlabel, ylabel=ylabel)
        return distr

    def remove(self, entry):
        self.entries.pop(entry, None)

    def total_entries(self):
        total = 0
        for count in self.entries.values():
            total += count
        return total

    def plot(self):
        import matplotlib.pyplot as plt
        plt.figure()
        plt.title(self.name)
        plt.bar(self.entries.keys(), self.entries.values())
        plt.xticks(list(self.entries.keys()))
        if self.xlabel is not None:
            plt.xlabel(self.xlabel)
        if self.ylabel is not None:
            plt.ylabel(self.ylabel)
        plt.show()
