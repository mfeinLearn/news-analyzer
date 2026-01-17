import re
# def word_count(word):
def word_count(word):
    # counts the number of occurrences of the specified word in the text.
    # print('this is in word_count: ', article)
    return article.count(word)


def most_common_word():
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

    

def average_word_length():
    #  calculates the average length of words in the text.
    words = article.split()

    if not words:
        return 0
    
    total_length = sum(len(word) for word in words )
    return total_length / len(words)





def number_of_paragraphs():
    # counts the number of paragraphs in the text.
    if not article.strip():
        return 0
    
    # Split into potential paragraphs using blank lines as separator
    paragraphs = article.split('\n\n')

    # Filter out completely empty entries and lines that are only whitespace
    #.. also count only paragraphs that have ≥ 15 words
    real_paragraphs = [para for para in paragraphs if para.strip() and len(para.split()) >= 15]
    return len(real_paragraphs)

if __name__ == '__main__':
    with open("News-Article-for-Python-Assessment.txt") as f:
        article = f.read()
        print(type( f.read()))
        print(word_count('ACME'))
        print(f'most_common_word VVV')
        print(most_common_word())
        print('number_of_paragraphs VVVV')
        print(number_of_paragraphs())
        print('average_word_length VVVV')
        print(average_word_length())