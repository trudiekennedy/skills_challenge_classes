class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents 
        self.words = contents.split()
        self.word_count = len(self.words)
        self.words_read = 0

    def format(self):
        return f"{self.title}: {self.contents}"
    
    def count_words(self):
        return self.word_count

    def reading_time(self, wpm):
        return self.word_count / wpm

    def reading_chunk(self, wpm, mins):
        words_for_session = wpm * mins
        if self.words_read >= self.word_count:
            self.words_read = 0
        
        start = self.words_read
        end = min(start + words_for_session, self.word_count)

        excerpt = self.words[start:end]
        self.words_read = end

        return " ".join(excerpt)


