# BookBot

BookBot is my first Boot.dev project!

## Purpose
This project is a text analyzer tool. It reads a generic text file (like an entire book) and generates a statistical report containing:
* **Total Word Count:** A count of every word found in the document.
* **Character Count:** A breakdown of the frequency of each alphanumeric character (non-alphanumeric characters are skipped).

## Getting Started

### 1. Get a Book
The repository does not contain book files. You will need to download a `.txt` file to your local machine to run the script.

You can find thousands of free books at [Project Gutenberg](https://www.gutenberg.org/).

Alternatively, here are direct links to the files used for testing:
* [Frankenstein](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/frankenstein.txt)
* [Moby Dick](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/mobydick.txt)
* [Pride and Prejudice](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/prideandprejudice.txt)

### 2. Run the Script
To run the project, use the following command in your terminal, replacing `<filepath_to_book>` with the path to your downloaded text file.

```bash
python3 main.py <filepath_to_book>
```

## Example Output
```bash
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
æ: 28
â: 8
ê: 7
ë: 2
ô: 1
============= END ===============
```
