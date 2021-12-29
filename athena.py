import wikipedia
import re
import random
from wiktionaryparser import WiktionaryParser
parser = WiktionaryParser()

quit_strings = ["quit$","^bye"]
pedia_strings = ["^(what|who|where) (is|are) "]
factoid_strings = ["tell me.* something"]
thank_strings = ["^thanks*( you)*"]
greet_strings = ["^hi","^hello","^hey"]
define_strings = ["^define "]

def get_input():
    #I'm sure this will be more complicated later.
    prompt = "Enter prompt: "
    return input(prompt)

def regex_bool(string,regex_array):
    for regex_exp in regex_array:
        pattern = re.compile(regex_exp)
        if pattern.match(string):
            return True
    return False

def get_wikipedia(prompt):
    #Have some code to parse any problems.
    raw_text = wikipedia.summary(prompt)
    clean_text = raw_text.encode("ascii","ignore").decode("ascii") #bruh
    return clean_text.replace("//","")

def get_wiktionary(prompt):
    #Add support for different languages in the future.
    word = parser.fetch(prompt)
    word_body = word[0]['definitions'][0]
    #dict_keys(['partOfSpeech', 'text', 'relatedWords', 'examples'])
    #Use every part.
    return word_body['text']

def parse_input(user_input):
    lower_input = user_input.lower()

    #There's got to be a better method than this.
    if regex_bool(lower_input,quit_strings):
        print("bye!")
        return False
    elif regex_bool(lower_input,pedia_strings):
        pattern = re.compile(pedia_strings[0])
        search_string = pattern.split(lower_input)[-1]
        print("i've read about {}:".format(search_string))
        summary = get_wikipedia(search_string)
        print(summary)
    elif regex_bool(lower_input,factoid_strings):
        prompt = wikipedia.random()
        print("i'll tell you about {}".format(prompt))
        summary = get_wikipedia(prompt)
        print(summary)
    elif regex_bool(lower_input,thank_strings):
        answers = ["no problem","don't worry about it","don't mention it","de nada","my pleasure"]
        random.shuffle(answers)
        print(answers[0])
    elif regex_bool(lower_input,greet_strings):
        print("yo")
    elif regex_bool(lower_input,define_strings):
        pattern = re.compile(define_strings[0])
        search_string = pattern.split(lower_input)[-1]
        print("i know what {} means:".format(search_string))
        summary = get_wiktionary(search_string)
        for line in summary:
            print(line)
    else:
        print("unrecognized input. sorry")
    return True

def main():
    continue_flag = True
    while continue_flag:
        user_input = get_input()
        continue_flag = parse_input(user_input)

if __name__ == '__main__':
    main()
