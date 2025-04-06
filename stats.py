def count_words(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

def count_chars(book_text):
    lower_text = book_text.lower()
    count_dict = {}
    for char in lower_text:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

def gen_report(count_dict):
    def sort_on(count_dict):
        return count_dict["count"]
    
    char_report = []
    current_chunk = {}

    for char, count in count_dict.items():
        current_chunk["character"] = char
        current_chunk["count"] = count
        char_report.append(current_chunk)
        current_chunk = {}

    char_report.sort(key=sort_on, reverse=True)
    
    return char_report
    
        
        