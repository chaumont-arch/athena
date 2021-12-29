import wikipedia

def get_input():
    #I'm sure this will be more complicated later.
    prompt = "Enter prompt: "
    return input(prompt)

def parse_input(user_input):
    lower_input = user_input.lower()
    if lower_input == "quit":
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