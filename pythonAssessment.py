import re
# def word_count(word):
def count_specific_word(article, word):
    # counts the number of occurrences of the specified word in the text.
    # print('this is in word_count: ', article)
    return article.count(word)


def identify_most_common_word(article):
    ## identifies the most common word in the text.
    
    # if article is empty, return none
    if not article:
        return None
    
    # if there is nothing in words then return none
    words = re.findall(r"[a-zA-Z0-9']+", article.lower())
    if not words:
        return None
    
    # frequency map to count the freq of all words in article
    freq_map = {}
    for word in words:
        freq_map[word] = freq_map.get(word,0) + 1
    
    # find word with max frequency
    max_count = 0
    res = None
    for word, count in freq_map.items():
        if count > max_count:
            max_count = count
            res = word

    return res

    

# def calculate_average_word_length(article):
#     #  calculates the average length of words in the text.
#     words = article.split()

#     if not words:
#         return 0
    
#     total_length = sum( len(word) for word in words )
#     return total_length / len(words)

import string

# def calculate_average_word_length(article):
#     words = article.split()
    
#     if not words:
#         return 0
    
#     # Strip punctuation from the start and end of each word
#     cleaned_words = [word.strip(string.punctuation) for word in words]
    
#     # Optional but recommended: filter out any empty strings that might result
#     # (e.g., if the text contained standalone punctuation like "!!!")
#     cleaned_words = [w for w in cleaned_words if w]
    
#     if not cleaned_words:
#         return 0
    
#     total_length = sum(len(word) for word in cleaned_words)
#     return total_length / len(cleaned_words)

def calculate_average_word_length(article):
    # If the article is empty or contains only whitespace → no words → average is 0.0
    if not article.strip():
        return 0.0
    
    words = article.split()
    
    # If split gave us nothing (very unlikely after the strip check, but safe)
    if not words:
        return 0.0
    
    # Strip punctuation from start and end of each word
    cleaned_words = []
    i = 0
    while i < len(words):
        cleaned = words[i].strip(string.punctuation)
        if cleaned:  # only keep if there's still content after stripping punctuation
            cleaned_words.append(cleaned)
        i += 1
    
    # After cleaning, if we have no valid words left (e.g. only punctuation was present)
    if not cleaned_words:
        return 0.0
    
    total_length = sum(len(word) for word in cleaned_words)
    return total_length / len(cleaned_words)

# def count_paragraphs(article):
#     # counts the number of paragraphs in the text.
#     if not article.strip():
#         return 0
    
#     # Split into potential paragraphs using blank lines as separator
#     paragraphs = article.split('\n\n')

#     # Filter out completely empty entries and lines that are only whitespace
#     #.. also count only paragraphs that have ≥ 15 words
#     real_paragraphs = [para for para in paragraphs if para.strip() and len(para.split()) >= 15]
#     return len(real_paragraphs)

# def count_paragraphs(article):
#     # counts the number of paragraphs in the text.
#     if not article.strip():
#         return 1
    
#     # Split into potential paragraphs using blank lines as separator
#     paragraphs = article.split('\n\n')

#     # Filter out completely empty entries and lines that are only whitespace
#     real_paragraphs = [para for para in paragraphs if para.strip()]
#     return len(real_paragraphs)

def count_paragraphs(article):
    if not article.strip():
        return 1
    
    paragraphs = article.split('\n\n')
    
    real_paragraphs = []
    index = 0
    length = len(paragraphs)
    
    while index < length:
        current_paragraph = paragraphs[index]
        stripped = current_paragraph.strip()
        if stripped != "":           
            real_paragraphs.append(current_paragraph)
        index = index + 1
    
    return len(real_paragraphs)

# def count_sentences(article):
#     if len(article) == 0:
#         return 1
#     # Split on sentence-ending punctuation followed by optional whitespace
#     sentences = re.split(r'[.!?]+', article)
#     # Filter out empty strings resulting from split
#     return len([s for s in sentences if s.strip()])

def count_sentences(article):
    if not article.strip():
        return 1
    
    sentences = re.split(r'[.!?]+', article)
    
    real_sentences = []
    i = 0
    while i < len(sentences):
        sentence = sentences[i]
        if sentence.strip():        
            real_sentences.append(sentence)
        i += 1
    
    return len(real_sentences)

if __name__ == '__main__':
    with open("News-Article-for-Python-Assessment.txt") as f:
        article = f.read()
        print(type( f.read()))
        print(f'count_specific_word VVVV')
        print(count_specific_word('ACME'))
        print(f'identify_most_common_word VVV')
        print(identify_most_common_word(article))
        print('count_paragraphs VVVV')
        print(count_paragraphs())
        print('count_sentences VVVV')
        print(count_sentences())