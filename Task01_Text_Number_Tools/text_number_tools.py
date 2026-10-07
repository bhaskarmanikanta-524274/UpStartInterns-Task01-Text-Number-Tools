def count_words(sentence):
    return len(sentence.split())

def find_longest_word(sentence):
    words = sentence.split()
    return max(words, key=len) if words else ""

def reverse_sentence(sentence):
    return sentence[::-1]

def is_prime(number):
    if number < 2: return False
    if number == 2: return True
    if number % 2 == 0: return False
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0: return False
        divisor += 2
    return True

def main():
    sentence = input("Enter a sentence: ").strip()
    try: number = int(input("Enter a number: ").strip())
    except ValueError:
        print("Invalid number. Please enter an integer."); return
    print("\n--- Results ---")
    print(f"Word Count: {count_words(sentence)}")
    print(f"Longest Word: {find_longest_word(sentence)}")
    print(f"Reversed Sentence: {reverse_sentence(sentence)}")
    print(f"Number: {number}")
    print(f"Prime: {'Yes' if is_prime(number) else 'No'}")

if __name__ == "__main__": main()
