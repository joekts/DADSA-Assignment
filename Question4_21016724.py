def frequency(file_string, number, file_string_2 = None):

    #Open the file and read the words into a list
    with open(file_string, 'r') as file:
        words = file.read().split()

    #Open the file and read the excluded words into a list
    with open("Romeo_excluded_words.txt", 'r') as file:
        excluded_words = file.read().split()

    #If a second file is given, read the words into a list
    if file_string_2 != None:
        with open(file_string_2, 'r') as file:
            words += file.read().split()

    #Convert all excluded words to lowercase
    for i, word in enumerate(excluded_words):
        excluded_words[i] = word.lower()

    #Initialise dictionary for words and their frequencies
    word_frequency = {}

    #Loop through list of words
    for word in words:

        word = word.lower()

        #If the word is in the excluded words list, skip it
        if word in excluded_words:
            continue

        word_frequency[word] = word_frequency.get(word, 0) + 1
        #Increase count of word in dictionary
        #if word in word_frequency:
         #   word_frequency[word] += 1
        #else:
         #   word_frequency[word] = 1

    #Sort the dictionary by value
    sorted_word_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

    #Initialise list for most frequent words
    most_frequent = []

    #Loop through sorted dictionary
    for i in range(number):
        #Add the word to the list
        most_frequent.append(sorted_word_frequency[i][0])

    return most_frequent


#Task 1
part_1 = frequency("Part1_Romeo_Joliete.txt", 30)
for word in part_1:
    print(word)

print("--------------------")

#Task 2
part_2 = frequency("Part2_Romeo_Joliete.txt", 30)
for word in part_2:
    print(word)

print("--------------------")

#Task 3
task_3 = frequency("Part1_Romeo_Joliete.txt", 20, "Part2_Romeo_Joliete.txt")
for word in task_3:
    print(word)