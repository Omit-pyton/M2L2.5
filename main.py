# Напишіть програму, яка читає вміст текстового файлу та виводить кількість слів у ньому.

file = open("text.txt", 'r', encoding='utf-8')
words = file.read()
words = words.split()
words_count = len(words)

print(words_count)

file.close()