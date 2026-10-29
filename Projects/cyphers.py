alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
import random
random.seed()
import math

def file_to_string(filename):
    with open(filename, "r", encoding="UTF8") as f:
        x = f.read()
    return x

def string_to_file(filename, s):
    with open(filename, "w", encoding="UTF8") as f:
        f.write(s)

def simplify_string(s):
    result = ""
    
    for char in s.upper():
        if "A" <=  char <= "Z":
            result += char
    
    return result

def num_to_let(x):
    letter = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "E",
        5: "F",
        6: "G",
        7: "H",
        8: "I",
        9: "J",
        10: "K",
        11: "L",
        12: "M",
        13: "N",
        14: "O",
        15: "P",
        16: "Q",
        17: "R",
        18: "S",
        19: "T",
        20: "U",
        21: "V",
        22: "W",
        23: "X",
        24: "Y",
        25: "Z"
    }
    
    return letter[x]

def let_to_num(a):
    number = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7,
        "I": 8,
        "J": 9,
        "K": 10,
        "L": 11,
        "M": 12,
        "N": 13,
        "O": 14,
        "P": 15,
        "Q": 16,
        "R": 17,
        "S": 18,
        "T": 19,
        "U": 20,
        "V": 21,
        "W": 22,
        "X": 23,
        "Y": 24,
        "Z": 25
    }
    return number[a]
    
def shift_char(char, shift):
    one = let_to_num(char)
    two = let_to_num(shift)
    
    shifting = (one + two) % 26
    
    shifted = num_to_let(shifting)
    return shifted

def caesar_enc(plain, key):
    result = ""
    
    for char in plain:
        result += shift_char(char, key)
    return result

def caesar_dec(cipher, key):
    result = ""
    backwards_key = -let_to_num(key)
    
    for char in cipher:
        backwards_shifting = (let_to_num(char) + backwards_key) % 26
        result += num_to_let(backwards_shifting)
    return result

def letter_counts(s):
    counts = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
        "F": 0,
        "G": 0,
        "H": 0,
        "I": 0,
        "J": 0,
        "K": 0,
        "L": 0,
        "M": 0,
        "N": 0,
        "O": 0,
        "P": 0,
        "Q": 0,
        "R": 0,
        "S": 0,
        "T": 0,
        "U": 0,
        "V": 0,
        "W": 0,
        "X": 0,
        "Y": 0,
        "Z": 0
    }
    
    for char in range(len(s)):
            counts[s[char]] = counts[s[char]] + 1
    return counts
    

def normalize(counts):
    
    total = sum(counts.values())
        
    for key, value in counts.items():
        counts[key] = value / total
    return counts

english_freqs = letter_counts(simplify_string(file_to_string("twocities_full.txt")))
english_freqs = normalize(english_freqs)

def distance(observed, expected):
    total = 0
    for letter in alpha:
        upper = observed[letter] - expected[letter]
        total += upper ** 2 / expected[letter]
    return total

def caesar_break(cipher, frequencies):
    best_key = None
    best_score = None

    for letter in alpha:
        plain_text = caesar_dec(cipher, letter)
        score = distance(normalize(letter_counts(plain_text)), frequencies)

        if best_score is None or score < best_score:
            best_score = score
            best_key = letter

    return [caesar_dec(cipher, best_key), best_key]

def vigenere_enc(plain, key):
    result = ""
    keynote = 0
    key_list = list(key)
    for i in plain:
        result += shift_char(i , key_list[keynote])
        keynote += 1
        if keynote > len(key) - 1:
            keynote = 0
            
    return result

def vigenere_dec(cipher, key):
    result = ""
    key_list = list(key)
    keynote = 0
    backwards_key = []
    for i in list(key):
        backwards_key.append(-let_to_num(i))
    
    for char in cipher:
        backwards_shifting = (let_to_num(char) + backwards_key[keynote]) % 26
        result += num_to_let(backwards_shifting)
        keynote += 1
        if keynote > len(key) - 1:
            keynote = 0
    return result

def split_string(s, parts):
    list = []
    for i in range(parts):
        list.append("")
        
    for index in range(len(s)):
        list[index % parts] += s[index]
        
    return list
    
def vig_break_for_length(cipher, klen, frequencies):
    sections = split_string(cipher, klen)
    key = ""
    decrypted_sections = []

    for section in sections:
        plaintext, letter = caesar_break(section, frequencies)
        key += letter
        decrypted_sections.append(plaintext)

    plaintext = ""
    for index in range(len(cipher)):
        section_number = index % klen
        position = index // klen
        plaintext += decrypted_sections[section_number][position]

    return [key, plaintext]

def vig_break(c, maxlen, frequencies):
    best_result = None
    best_score = None

    for klen in range(1, maxlen + 1):
        result = vig_break_for_length(c, klen, frequencies)
        plaintext = result[1]
        score = distance(normalize(letter_counts(plaintext)), frequencies)

        if best_score is None or score < best_score:
            best_score = score
            best_result = result

    return best_result
    
def sub_gen_key():
    letters = list(alpha)
    random.shuffle(letters)
    return "".join(letters)


def sub_enc(s, k):
    result = ""

    for letter in s:
        index = alpha.index(letter)
        result += k[index]

    return result

def sub_dec(c, k):
    result = ""

    for letter in c:
        index = k.index(letter)
        result += alpha[index]

    return result

def count_trigrams(s):
    counts = {}

    for i in range(len(s) - 2):
        trigram = s[i:i + 3]
        counts[trigram] = counts.get(trigram, 0) + 1

    return counts

english_trigrams = count_trigrams(simplify_string(file_to_string("twocities_full.txt")))
normalize(english_trigrams)

def map_log(frequencies):
    for trigram in frequencies:
        frequencies[trigram] = math.log(frequencies[trigram])

    return frequencies

map_log(english_trigrams)

def trigram_score(s, frequencies):
    score = 0

    for i in range(len(s) - 2):
        trigram = s[i:i + 3]
        score += frequencies.get(trigram, -15)

    return score

def sub_break(cipher, frequencies):
    best_key = None
    best_plaintext = None
    best_score = float("-inf")

    for _ in range(20):
        key = sub_gen_key()
        plaintext = sub_dec(cipher, key)
        score = trigram_score(plaintext, frequencies)
        failed_swaps = 0

        while failed_swaps < 1000:
            candidate = list(key)
            i, j = random.sample(range(26), 2)
            candidate[i], candidate[j] = candidate[j], candidate[i]
            candidate = "".join(candidate)

            candidate_text = sub_dec(cipher, candidate)
            candidate_score = trigram_score(candidate_text, frequencies)

            if candidate_score > score:
                key = candidate
                plaintext = candidate_text
                score = candidate_score
                failed_swaps = 0
            else:
                failed_swaps += 1

        if score > best_score:
            best_key = key
            best_plaintext = plaintext
            best_score = score

    return best_key, best_plaintext
