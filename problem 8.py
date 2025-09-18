class StringReverser:
    def reverse_words(self, text):
        words = text.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

#input string
input_str = input("enter a string: ")

#create object and reverse
reverser = StringReverser()
result = reverser.reverse_words(input_str)

print("Reversed string word by word:", result)

