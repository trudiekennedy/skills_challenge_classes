

class GrammarStats:
    def __init__(self):
        self.passed_check = 0
        self.failed_check = 0

    def check(self, text):
        if text == "":
            raise Exception("No text to analyse!")
        if text[0].isupper() and text[-1] in ["!", "?", "."]:
            self.passed_check += 1
            return True
        else:
            self.failed_check += 1
            return False

    def percentage_good(self):
        total = self.passed_check + self.failed_check
        return round(self.passed_check/total * 100)
