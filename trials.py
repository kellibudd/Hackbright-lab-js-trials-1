"""Python functions for JavaScript Trials 1."""


def output_all_items(items):

    for item in items:
        print(item)

def get_all_evens(nums):

    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums


def get_odd_indices(items):
    
    odd_indices = []

    for idx, item in enumerate(items):
        if idx % 2 != 0:
            odd_indices.append(item)

    return odd_indices


def print_as_numbered_list(items):
    
    i = 1

    for item in items:
        print(f'{i}. {item}')
        i += 1


def get_range(start, stop):

    range_of_nums = []

    for num in range(start,stop):
        if num < stop:
            range_of_nums.append(num)

    return range_of_nums

def censor_vowels(word):

    censored_word = []
    
    for letter in word:
        if letter in 'aeiou':
            censored_word.append('*')
        else:
            censored_word.append(letter)

    return ''.join(censored_word)

def snake_to_camel(string):
    
    upper_camel_case = []

    for word in string.split('_'):
        upper_camel_case.append(f'{word[0].upper()}{word[1:].lower()}')

    return ''.join(upper_camel_case)


def longest_word_length(words):

    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)

    return longest

def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
