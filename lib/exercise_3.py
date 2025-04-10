def get_most_common_letter(text):
    counter = {}
    for char in text:
        counter[char] = counter.get(char, 0) + 1
    
    # get rid of punctuation and spaces
    for char in list(counter.keys()):
        if not char.isalpha():
            del counter[char]

    letter = sorted(counter.items(), key=lambda item: -item[1])[0][0]
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
