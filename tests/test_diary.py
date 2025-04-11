from lib.diary import DiaryEntry

def test_format():
    diary_entry = DiaryEntry("10th April 2025", "There was a woman named Trudie...")
    result = diary_entry.format()
    assert result == "10th April 2025: There was a woman named Trudie..."

def test_count_words():
    diary_entry = DiaryEntry("10th April 2025", "Frogs " * 200)
    diary_entry.format()
    result = diary_entry.count_words()
    assert result == 200

def test_reading_time():
    diary_entry = DiaryEntry("10th April 2025", "Frogs " * 200)
    diary_entry.format()
    diary_entry.count_words()
    result = diary_entry.reading_time(200)
    assert result == 1.0

def test_reading_chunk():
    diary_entry = DiaryEntry("10th April 2025", "Frogs " * 200)
    diary_entry.format()
    diary_entry.count_words()
    assert diary_entry.reading_chunk(2, 3) == "Frogs Frogs Frogs Frogs Frogs Frogs"

def test_next_chunk():
    diary_entry = DiaryEntry("10th April 2025", "Frogs go ribbit ribbit ribbit all day long")
    diary_entry.format()
    diary_entry.count_words()
    diary_entry.reading_chunk(2, 1)
    assert diary_entry.reading_chunk(2, 1) == "ribbit ribbit"

def test_chunk_to_the_end():
    diary_entry = DiaryEntry("10th April 2025", "Frogs go ribbit ribbit ribbit all day long")
    diary_entry.format()
    diary_entry.count_words()
    diary_entry.reading_chunk(3, 1)
    diary_entry.reading_chunk(3, 1)
    assert diary_entry.reading_chunk(3, 1) == "day long"

def test_chunk_from_beginning():
    diary_entry = DiaryEntry("10th April 2025", "Frogs go ribbit ribbit ribbit all day long")
    diary_entry.format()
    diary_entry.count_words()
    diary_entry.reading_chunk(4, 2)
    assert diary_entry.reading_chunk(4, 1) == "Frogs go ribbit ribbit"