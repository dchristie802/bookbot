def get_word_count(text):
  words = text.split()
  return len(words)

def get_char_count(text):
  char_counts = {}
  for char in text:
    char_lowercase = char.lower()
    if char_lowercase in char_counts:
      char_counts[char_lowercase] += 1
    else:
      char_counts[char_lowercase] = 1
  return char_counts

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
  dict_list = []
  for key in dict:
    dict_list.append({
      "char": key,
      "num": dict[key]
    })

  dict_list.sort(reverse=True, key=sort_on)
  return dict_list
