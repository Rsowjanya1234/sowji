numbers = []
words = []

# Input loop for numbers
while True:
    try:
        num = float(input("Enter a number (0 to stop): "))
        if num == 0:
            break
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Input loop for words
while True:
    word = input("Enter a word (END to stop): ")
    if word == "END":
        break
    words.append(word)

# Sort and print numbers
if numbers:
    sorted_numbers_asc = sorted(numbers)
    sorted_numbers_desc = sorted(numbers, reverse=True)
    print("Numbers in ascending order:", sorted_numbers_asc)
    print("Numbers in descending order:", sorted_numbers_desc)
else:
    print("No numbers entered.")

# Sort and print words
if words:
    sorted_words_asc = sorted(words)
    sorted_words_desc = sorted(words, reverse=True)
    print("Words in ascending order:", sorted_words_asc)
    print("Words in descending order:", sorted_words_desc)
else:
    print("No words entered.")
