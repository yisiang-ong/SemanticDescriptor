'''Semantic Similarity: starter code

'''

import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 2.
    '''

    sum_of_squares = 0.0  # floating point to handle large numbers
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    '''Return the cosine similarity of sparse vectors vec1 and vec2,
    stored as dictionaries as described in the handout for Project 2.
    '''

    dot_product = 0.0  # floating point to handle large numbers
    for x in vec1:
        if x in vec2:
            dot_product += vec1[x] * vec2[x]

    # Make sure empty vectors don't cause an error -- return -1 as
    # suggested in the handout for Project 2.
    norm_product = norm(vec1) * norm(vec2)
    if norm_product == 0.0:
        return -1.0
    else:
        return dot_product / norm_product


def get_sentence_lists(text):
    con1 = ''
    con2 = []
    temp = ''
    textlist = list(text)
    #remove punctuations(not . ? !)
    for x in range(len(textlist)):
        if textlist[x] == ',' or textlist[x] == ':' or textlist[x] == ';' or textlist[x] == '"' or textlist[x] == "'" \
        or textlist[x] == '-' or textlist[x] == '--' or textlist[x] == '(' or textlist[x] == ')':
            textlist[x] = ' '
    text = ''.join(textlist)
    #separate sentences by these punctuations: . ? !
    for i in text:
        if i == '.' or i == '?' or i == '!':
            if temp != '':
                con1 += temp
                temp = ''
        else:
            temp += i
        if i == '.' or i == '?' or i == '!':
            temp1 = con1.split()
            if temp1 != []:
                con2.append(temp1)
                con1 = ''
    return con2
    pass


def get_sentence_lists_from_files(filenames):
    files = {}
    #read file content and join them as a list by using get_sentence_lists function
    for filename in filenames:
        with open(filename, 'r') as file:
            if filename in files:
                continue
            files[filename] = file.readlines()
    for filename, text in files.items():
        pass
    file.close()
    text = ''.join(text)
    return get_sentence_lists(text)




def build_semantic_descriptors(sentences):
    final_dict = {}
    #generate a dictionary for key words
    for sen in sentences:
        for key in sen:
            if key not in final_dict:
                #generate sub-dictionary
                final_dict[key] = {}
    #put words and words number into sub-dictionary
    for key in final_dict:
        for sen2 in sentences:
            if key in sen2:
                for word in sen2:
                    #add words into sub-dictionary and count the number of word
                    if word != key and word not in final_dict[key]:
                        final_dict[key][word] = 1
                    elif word in final_dict[key]:
                        final_dict[key][word] += 1
    return(final_dict)

def most_similar_word(word, choices, semantic_descriptors):
    dict_sim = {}
    list = []
    for i in range(len(choices)):
        #if the word is not in semantic descriptors, set sim as -1
        if word not in semantic_descriptors or choices[i] not in semantic_descriptors:
            sim = -1
        else:
            #calculate the similarity of words by using cosine similarity function
            dict_word = semantic_descriptors[word]
            sim = cosine_similarity(dict_word, semantic_descriptors[choices[i]])
        dict_sim[choices[i]] = sim
    #find the largest similarity words and add it to the list
    max_key = max(dict_sim, key=dict_sim.get)
    list.append(max_key)
    #return the word that first get into the list
    return list[0]
    pass


def run_similarity_test(filename, semantic_descriptors):
    #read test file
    file = open(filename, 'r')
    templist = file.readlines()
    #replace \n by . and add . at the end of test text
    for i in range(len(templist)):
        templist[i] = templist[i].replace("\n", '.')
        if i == len(templist) - 1:
            templist[i] = templist[i] + '.'
    text = "".join(templist)
    List = get_sentence_lists(text)
    length = len(List)
    count = 0
    for line in List:
        #extract word, choices from the test text
        question = line[0]
        print('Question: ',end='')
        print(question)
        choices = line[2:]
        print('choices: ',end='')
        print(choices)
        guess = most_similar_word(question, choices, semantic_descriptors)
        correct = line[1]
        print('correct answer: ',end='')
        print(correct)
        print('guessed answer: ',end='')
        print(guess)
        print()
        #count correct number
        if guess == correct:
            count += 1
    percentage = count/length
    print('correct persentage: ',end='')
    print(percentage)
    return percentage
    pass


# test code for Q1 (a):
text1 = 'I am a sick man. I am a spiteful man. I am an unattractive man. I believe my liver is diseased.\
However, I know nothing at all about my disease, and do not know for certain what ails me.'
sentence1 = get_sentence_lists(text1)
#print(sentence1)

# test code for Q1 (b):
filenames = ['swex.txt','wpex.txt']
#print(get_sentence_lists_from_files(filenames))

# test code for Q1 (c):
text2 = 'I am a sick man. I am a spiteful man. I am an unattractive man. I believe my liver is diseased.\
However, I know nothing at all about my disease, and do not know for certain what ails me.'
sentence2 =get_sentence_lists(text2)
semantic_descriptor = build_semantic_descriptors(sentence2)
print(semantic_descriptor)

# test code for Q1 (d):
#text3 = 'watch see hear see.'
#sentence3 = get_sentence_lists(text3)
#semantic_descriptor3 = build_semantic_descriptors(sentence3)
#word = 'watch'
#choices = ['see','hear','see']
#sim_word = most_similar_word(word,choices,semantic_descriptor3)
#print(sim_word)

# test code for Q3 and Q1 part(e):
#filenames = 'test.txt'
#sentence_list = get_sentence_lists_from_files(['sw.txt','wp.txt'])
#semantic_descriptors = build_semantic_descriptors(sentence_list)
#print(semantic_descriptors)
#run_similarity_test(filenames,semantic_descriptors)