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

        # If we've read the whole text, reset words read back to zero to begin the chunk again.
        if self.words_read >= self.word_count:
            self.words_read = 0
        
        # Find the index for our chunk of text to be read in session.
        # Uses the indexes to get the chunk of words for our excerpt. 
        start = self.words_read
        end = min(start + words_for_session, self.word_count) # Makes sure word count isn't exceeded.
        excerpt = self.words[start:end]
        
        # Updates the words_read so that program knows how far the text has been read.
        self.words_read = end

        return " ".join(excerpt)


