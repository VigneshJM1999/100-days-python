from morse import string_list, morse_list
from art import logo

def morse(user_text, encode_or_decode):
    final_output = ''
    if encode_or_decode.lower() == "encode":
        morse_output = [morse_list[string_list.index(i.upper())] for i in user_text]
        final_output = ' '.join(morse_output)

    elif encode_or_decode.lower() == "decode":
        string_output = [string_list[morse_list.index(i)] for i in user_text.strip().split(' ')]
        final_output = ''.join(string_output)

    else:
        print("Please enter a valid option")
        return

    print(f"Here is the {encode_or_decode}d result: {final_output}")


print(logo)

should_continue = True
while should_continue:

    user_input = input("Please enter your string to encode: ")
    encode_decode = input("Encode or Decode? ")
    morse(user_input, encode_decode)

    user_response = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if user_response == "no":
        should_continue = False
        print("GoodBye!")