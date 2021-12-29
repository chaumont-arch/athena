import wikipedia
import re

quit_strings = ["quit","bye.?"]

def get_input():
    #I'm sure this will be more complicated later.
    prompt = "Enter prompt: "
    return input(prompt)

def regex_bool(string,regex_array):
    for regex_exp in regex_array:
        if len(re.findall(regex_exp,string)) > 0:
            return True
    return False

def parse_input(user_input):
    lower_input = user_input.lower()
   # if lower_input == "quit":
    #    return False
    if regex_bool(lower_input,quit_strings):
        print("bye!")
        return False
    else:
        print("unrecognized input")
    return True

def main():
    continue_flag = True
    while continue_flag:
        user_input = get_input()
        continue_flag = parse_input(user_input)

if __name__ == '__main__':
    main()