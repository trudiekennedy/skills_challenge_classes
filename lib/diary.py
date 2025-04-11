class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents 
        self.word_count = 0
        self.words =[]
        self.words_read = 0
        self.words_remaining = 0

    def format(self):
        self.entry = f"{self.title}: {self.contents}"
        return self.entry
    
    def count_words(self):
        self.words = self.contents.split()
        self.word_count = len(self.words)
        self.words_remaining = len(self.words)
        return self.word_count

    def reading_time(self, wpm):
        return self.word_count / wpm

    def reading_chunk(self, wpm, mins):
        words_for_session = wpm * mins
        if self.words_remaining > 0:
            excerpt = self.words[self.words_read:self.words_read + words_for_session]
            self.words_read += len(excerpt)
            self.words_remaining -= len(excerpt)
            return " ".join(excerpt)
        else:
            self.words_remaining = self.word_count
            self.words_read = 0
            excerpt = self.words[:words_for_session]
            self.words_read += len(excerpt)
            self.words_remaining -= len(excerpt)
            return " ".join(excerpt)


