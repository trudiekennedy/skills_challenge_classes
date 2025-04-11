

class GrammarStats:
    def __init__(self):
        pass

    def check(self, text):
        if text == "":
            raise Exception("No text to analyse!")
        return text[0].isupper() and text[-1] in ["!", "?", "."]

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        pass
