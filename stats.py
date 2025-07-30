def get_num_words(book_text):
    split_words = book_text.split()
    num_words = len(split_words)
    return num_words

def letter_list(book_text):
    letter_count = {}
    lowercase = book_text.lower()
    for letter in lowercase:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    return letter_count

def num_breakout(letters):
    return letters["num"]

def better_list(final_sorted):
    best_list = []
    for letter, count in final_sorted.items():
        new_broken_out ={
            "char":letter,
            "num": count
            }
        best_list.append(new_broken_out)
    best_list.sort(reverse=True, key=num_breakout)
    return best_list