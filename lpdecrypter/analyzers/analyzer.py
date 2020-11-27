
DISPLAY_TEXT = 0
DISPLAY_PLOT = 1

class Analyzer(object):

    """
        An Analyzer is an object that does some kind of analisys on ciphertext and or plaintext
    """
    def analyze(self, data):
        """
            Analyzes the given data
        """
        pass

    def display(self, analysis_results, display_method='text'):
        """
            Displays analisis results in some way (text or plots)
        """
        pass
