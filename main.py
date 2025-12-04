import sys
from stats import get_word_count, get_char_count, sort_dict

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  book_file_path = sys.argv[1]
  book_text = get_book_text(book_file_path)
  word_count = get_word_count(book_text)
  char_count_sorted_by_count = sort_dict(get_char_count(book_text))

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_file_path}...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")
  for char_count in char_count_sorted_by_count:
    char = char_count["char"]
    if char.isalpha():
      print(f"{char}: {char_count["num"]}")
  print("============= END ===============")

main()
