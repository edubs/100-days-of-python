letters  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    shifted_text = ""
    if direction == "decode":
        shift = 0 - shift
    for t in text:
        if t in letters:
            position = letters.index(t)
            new_position =  position + shift
            shifted_text+=letters[new_position]
        else:
            shifted_text+=t
    print(f"The {direction}d text is: {shifted_text}")

def run_caesar(go_again):
    if go_again == 'yes':
        direction = input("Type 'encode' to encrypt type 'decode' to decrypt:\n")
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        if shift > 26:
            shift %= 26
        caesar(text, shift, direction)
        run_caesar(input("type 'yes' to start again, otherwise type 'no'\n"))
    else:
        print("goodbye!")


run_caesar("yes")