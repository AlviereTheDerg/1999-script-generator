
import dominate.svg
import eng_to_ipa as eti
import dominate
from dominate.tags import *
from dominate.svg import *

display_width = 4000
wide_consonant_width = 120
thin_consonant_width = 40
vowel_size = 40
row_height = 300
character_gap = 10
space_width = wide_consonant_width - character_gap
thin_consonants = {'m', 'n', 'h', 'l'}
paths = {
    "r":  "m110 0 v20 h-20 v-7.5 a140 110 0 0 0 -69.25 107.5 h69.25 v-10 h20 v20 h-107.1 a140 110 0 0 1 107.1 -130 Z",
    "d":  "m110 0 v200 h10 v10 h-30 v-80 h-87.1 a140 110 0 0 1 107.1 -130 m-20 12.5 a140 110 0 0 0 -69.25 107.5 h69.25 v-107.5 Z",
    "b":  "m110 0 v200 h10 v10 h-30 v-70 a140 110 0 0 1 -90 70 v-7.5 a140 110 0 0 0 75 -72.5 h-72.1 a140 110 0 0 1 107.1 -130 m-20 120 v-107.5 a140 110 0 0 0 -69.25 107.5 h69.25 Z",
    "ð":  "m110 0 v200 h10 v10 h-30 v-80 h-87.1 a140 110 0 0 1 107.1 -130 m-20 12.5 a140 110 0 0 0 -69.25 107.5 h29.25 v-55 h40 v-52.5 m0 107.5 v-45 h-25 v45 h25 Z",
    "v":  "m110 0 v200 h10 v10 h-30 v-70 a140 110 0 0 1 -90 70 v-7.5 a140 110 0 0 0 75 -72.5 h-72.1 a140 110 0 0 1 107.1 -130 m-20 120 v-45 h-40 v-35.4 a140 110 0 0 0 -29.25 80.4 h69.25 m0 -55 v-52.5 a140 110 0 0 0 -25 14.4 v38.1 h25 Z",

    "g":  "h110 v5 a140 110 0 0 0 -90 100 v95 h70 v-70 h-10 v-10 h30 v90 h-110 v-105 a140 110 0 0 1 89 -100 h-69 v10 h-20 v-15 Z",
    "ŋ":  "h110 v5 a140 110 0 0 0 -90 100 v95 h30 v-80 h60 v90 h-110 v-105 a140 110 0 0 1 89 -100 h-69 v10 h-20 v-15 m90 130 h-25 v70 h25 v-70 Z",

    "t":  "m110 0 v200 h10 v10 h-30 v-197.5 a140 110 0 0 0 -65 66 h-25 v-25 h18 a140 110 0 0 1 92 -53.5 Z",
    "θ":  "m110 0 v200 h10 v10 h-70 v-90 h40 v-107.5 a140 110 0 0 0 -65 66 h-25 v-25 h18 a140 110 0 0 1 92 -53.5 m-20 130 h-25 v70 h25 v-70 Z",

    "dʒ": "h110 v5 a140 110 0 0 0 -89.25 115 h89.25 v80 h10 v10 h-30 v-80 h-87.1 a140 110 0 0 1 86.1 -125 h-69 v10 h-20 v-15 Z",
    "tʃ": "h110 v5 a140 110 0 0 0 -89.25 115 h29.25 v-55 h60 v55 v80 h10 v10 h-30 v-80 h-87.1 a140 110 0 0 1 86.1 -125 h-69 v10 h-20 v-15 m90 120 v-45 h-25 v45 h25 Z",

    "s":  "h110 v210 a140 110 0 0 1 -109.4 -90 h20.4 a140 110 0 0 0 69 77.5 v-192.5 h-70 v10 h-20 v-15 Z",
    "ʃ":  "h110 v210 a140 110 0 0 1 -109.4 -90 h20.4 a140 110 0 0 0 69 77.5 v-122.5 h-40 v-70 h-30 v10 h-20 v-15 m90 5 h-25 v60 h25 v-60 Z",
    "z":  "h110 v210 a140 110 0 0 1 -109.4 -90 h89.4 v-115 h-70 v10 h-20 v-15 m90 130 h-66.25 a140 110 0 0 0 66.25 67.5 v-67.5 Z",
    "ʒ":  "h110 v210 a140 110 0 0 1 -109.4 -90 h49.4 v-115 h-30 v10 h-20 v-15 m90 130 h-66.25 a140 110 0 0 0 66.25 67.5 v-67.5 m0 -10 v-115 h-25 v115 h25 Z",

    "p":  "m110 0 v130 h-86.25 a140 110 0 0 0 66.25 67.5 v-7.5 h20 v20 a140 110 0 0 1 -109.4 -90 h89.4 v-107.5 a140 110 0 0 0 -65 66 h-25 v-25 h18 a140 110 0 0 1 92 -53.5 Z",
    "f":  "m110 0 v130 h-86.25 a140 110 0 0 0 66.25 67.5 v-7.5 h20 v20 a140 110 0 0 1 -109.4 -90 h49.4 v-80.4 a140 110 0 0 0 -25 38.9 h-25 v-25 h18 a140 110 0 0 1 92 -53.5 m-20 120 v-107.5 a140 110 0 0 0 -25 14.4 v93.1 h25 Z",

    "k":  "h30 v117.5 a140 110 0 0 0 69.25 -107.5 h-10 v-10 h27.85 a140 110 0 0 1 -87.1 125.35 v74.65 h10 v10 h-30 v-200 h-10 v-10 Z",
    "x":  "h30 v55 h40 v35.4 a140 110 0 0 0 29.25 -80.4 h-10 v-10 h27.85 a140 110 0 0 1 -87.1 125.35 v74.65 h10 v10 h-30 v-200 h-10 v-10 m30 65 v52.5 a140 110 0 0 0 25 -14.4 v-38.1 h-25 Z",
    
    "m":  "h30 v200 h10 v10 h-30 v-200 h-10 v-10 Z",
    "n":  "h30 v200 h10 v10 h-30 v-120 h-10 v-10 h10 v-70 h-10 v-10 Z",

    "h":  "h30 v120 h10 v10 h-30 v-120 h-10 v-10 Z",
    "l":  "h30 v10 h-10 v70 h10 v10 h-10 v30 h10 v10 h-30 v-130 Z",

    # vowels
    "eɪ": "m-20 -40 h12.5 v30 a15 30 0 0 0 15 -30 h12.5 v40 h-12.5 v-10 a20 30 0 0 1 -15 10 h-12.5 v-40 Z",
    "i":  "m-7.5 -40 h15 v40 h-15 v-40 Z",
    "aɪ": "m-20 0 a80 50 0 0 1 40 -40 v10 a50 50 0 0 0 -10 6 l10 24 h-10 l-7.5 -18.5 a50 50 0 0 0 -12.5 18.5 h-10 Z",
    "oʊ": "a20 20 0 0 0 0 -40 a20 20 0 0 0 0 40 m0 -10 a10 10 0 0 1 0 -20 a10 10 0 0 1 0 20 Z",
    "u":  "m-7.5 -25 l15 -5 v15 l-15 5 v-15 Z",

    "ɑ":  "m-20 -40 h40 a40 50 0 0 1 -25 30 h25 v10 h-40 v-10 a60 80 0 0 0 20 -20 h-20 v-10 Z",
    "ɪ":  "m-20 -40 h40 v40 h-13 v-30 h-14 v30 h-13 v-40 Z",
    "ɛ":  "m-20 -40 h12.5 v30 a15 35 0 0 0 15 -30 h12.5 a30 40 0 0 1 -22.5 40 h-17.5 v-40 Z",
    "ʌ":  "m-20 -40 h20 a20 20 0 0 1 0 40 h-20 v-10 h18 a10 10 0 0 0 0 -20 h-18 v-10 Z",
    
    "æ":  "m20 -40 a40 50 0 0 1 -40 40 v-10 a30 50 0 0 0 25 -30 h15 Z",
    "ɔ":  "m-20 -40 h20 a20 20 0 1 1 -20 20 h10 a10 10 0 1 0 10 -10 h-20 v-10 Z",

    #punctuation
    ".": "m0 130 v-10 h30 v-10 h15 v20 h-45 m110 0 h-45 v-20 h15 v10 h30 v10 Z",
    ",": "m0 130 v-10 h30 v-10 h15 v20 h-45 Z",
    "!": "m0 130 v-10 h30 v-60 h15 v70 h-45 m110 0 h-45 v-70 h15 v60 h30 v10 Z",
    "?": "m0 130 v-10 h30 v-10 h15 v20 h-45 m110 0 h-45 v-20 h15 v10 h30 v10 m-65 -40 h-15 v-30 h15 v30 m20 0 v-30 h15 v30 h-15 Z",
    "-": "m30 130 h50 v-10 h-50 v10 Z"
}
consonants = { "r","d","b","ð","v", "g","ŋ", "t","θ", "dʒ","tʃ", "s","ʃ","z","ʒ", "p","f", "k","x", "m","n", "h","l" }
vowels = { "eɪ","i","aɪ","oʊ","u", "ɑ","ɪ","ɛ","ʌ", "æ","ɔ" }
punctuation = { " ",".",",","!","?","-" }

def get_consonant_width(consonant):
    return thin_consonant_width if (consonant in thin_consonants) else wide_consonant_width

def path_consolidator_unit(*characters):
    consonant = characters[-1]
    vowels = characters[:-1]
    output = [(0, 0, consonant)] # -> (x, y, symbol)
    if len(vowels) == 1:
        output.append((get_consonant_width(consonant) / 2, -character_gap, vowels[0]))
    if len(vowels) == 2:
        midpoint = get_consonant_width(consonant) / 2
        offset = (character_gap + vowel_size) / 2
        output.append((midpoint - offset, -character_gap, vowels[0]))
        output.append((midpoint + offset, -character_gap, vowels[1]))
    def get_display_coords_letter(input_x):
        for x,y,character in output:
            yield (x+input_x, y, character)
    return get_display_coords_letter, get_consonant_width(consonant) # -> generator to retrieve

def path_consolidator_word(entries):
    existing_offset = 0
    results = []
    for entry in entries:
        if entry == [" "]:
            existing_offset += space_width
            continue
        buffer, width = path_consolidator_unit(*entry)
        results.extend(list(buffer(existing_offset)))
        existing_offset += width + character_gap
    def get_display_coords_word(input_x, input_y):
        augmented_y = input_y + vowel_size + character_gap
        for x,y,symbol in results:
            yield (x+input_x, y+augmented_y, symbol)
    return get_display_coords_word, existing_offset

def collapse_vowel_stack(base, vowel_stack: list):
    unit_stack = []
    while vowel_stack:
        unit = [base, vowel_stack.pop()]
        if base not in thin_consonants and vowel_stack:
            unit.append(vowel_stack.pop())
        unit_stack.append(unit[::-1])
        base = 'h'
    return unit_stack[::-1]

def collect_to_syllable_units(tokens):
    output = []
    vowel_stack = []
    for token in tokens:
        if token in vowels:
            vowel_stack.append(token)
            continue
        if len(vowel_stack) == 0:
            output.append([token])
            continue
        if token in punctuation:
            output.extend(collapse_vowel_stack('h', vowel_stack))
            output.append([token])
            continue
        if token in consonants:
            output.extend(collapse_vowel_stack(token, vowel_stack))
            continue
        print("BIG UH OH", token, vowel_stack)
    if vowel_stack:
        output.extend(collapse_vowel_stack('h', vowel_stack))
    return output


monophthong_subs = {
    # consonants
    "p":"p","b":"b","t":"t","d":"d","k":"k",
    "g":"g","ʧ":"tʃ","ʤ":"dʒ","f":"f","v":"v",
    "θ":"θ","ð":"ð","s":"s","z":"z","ʃ":"ʃ",
    "ʒ":"ʒ","x":"x","h":"h","m":"m","n":"n",
    "ŋ":"ŋ","j":"i","w":"u","r":"r","l":"l",

    #vowels
    "ɪ":"ɪ", "i":"i", "ʊ":"u", "u":"u", "ɛ":"ɛ", "ə":"ʌ", "ɜ":"ʌ", "ʌ":"ʌ", "æ":"æ", "ɑ":"ɑ", "ɔ":"ɔ",

    #punctuation
    ".":".", ",":",", "!":"!", "?":"?"
}
diphthong_opens = {"e","o","a","a"}
diphthong_subs = {
    #vowels
    "eɪ":"eɪ", "oʊ":"oʊ", "aɪ":"aɪ", "aʊ":"ɔ"
}
special_ignores = {"ˈ","ˌ"}
def process_word(text):
    IPA = eti.convert(text)
    if IPA[-1] == '*':
        print("ERROR PROCESSING WORD:", text)
        return []
    
    tokens = []
    letter_iter = iter(IPA)
    while token := next(letter_iter, False):
        if holder := monophthong_subs.get(token, None):
            tokens.append(holder)
            continue
        if token in diphthong_opens:
            token += next(letter_iter)
            tokens.append(diphthong_subs.get(token))
            continue
        if token in special_ignores:
            continue
        print("ERROR PROCESSING CHARACTER:", token)
    return tokens

def process_text(text: str):
    border = 10
    horizontal_position = vertical_position = border
    for word in text.split():
        word = process_word(word)
        units = collect_to_syllable_units(word)
        path_func,width = path_consolidator_word(units)
        if horizontal_position + width > display_width:
            horizontal_position = border
            vertical_position += row_height
        for x,y,character in path_func(horizontal_position, vertical_position):
            path(d="".join([f"M{x} {y}", paths.get(character, "h5")]))
        horizontal_position += width + space_width

if __name__ == '__main__':
    doc = dominate.document(title="")
    with doc.head:
        style(
            """
            """
        )
    with doc:
        with svg():
            attr(height=8000, width=display_width)
            if False: # printing testcard
                for x,y,character in path_consolidator_word([["i","p"],["ɪ","b"],["ɛ","t"],["æ","d"],["ɑ","s"],["ʌ","z"],["oʊ","dʒ"],["u","k"],["eɪ","g"],["aɪ","m"],["n"],["ɔ","h"],["r"],["l"]])[0](10,10):
                    path(d="".join([f"M{x} {y}", paths.get(character, "h5")]))
                for x,y,character in path_consolidator_word([["f"],["v"],["θ"],["ð"],["ʃ"],["ʒ"],["tʃ"],["x"],["ŋ"]])[0](10,310):
                    path(d="".join([f"M{x} {y}", paths.get(character, "h5")]))
            else:
                process_text(input("Please input your text:"))
    with open("output.html", 'w') as f:
        f.write(str(doc))