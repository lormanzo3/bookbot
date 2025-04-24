def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    characters = {}
    for c in text:
        lowered = c.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters


def get_sorted_list(character_count):
    char_list = []
    for char, count in character_count.items():
        char_dict = {"char": char, "num": count}
        char_list.append(char_dict)
    
    def sort_c(dict_item):
        return dict_item["num"]
    
    char_list.sort(reverse=True, key=sort_c)
    return char_list
    
