### Zablos Substitution Cipher 1.0.1 ###
# for those who are bored with Sudoku :D
# encrypts text with random substition mapping
# difficulty 2 replaces spaces with a random sign
# difficulty 3 masks doubled signs with "repeat previous sign" AA -> AX
import random
import string

def generate_substitution():
    letters = list(string.ascii_uppercase) + ["+", "-"]
    shuffled = letters[:]
    random.shuffle(shuffled)
    return dict(zip(letters, shuffled))

def clean_text(text):
    letter = list(string.ascii_uppercase) + [" "]
    cleaned = ""
    text = text.upper()
    for ch in text:
        if ch in letter or ch == " ":
            cleaned += ch
        elif ch == "Ä":
            cleaned += "AE"
        elif ch == "Ö":
            cleaned += "OE"
        elif ch == "Ü":
            cleaned += "UE"
    return cleaned

def encrypt(text, cipher):
    return "".join(cipher.get(ch, ch) for ch in text)

def print_mapping(cipher):
    print("Cipher mapping:")
    for k, v in cipher.items():
        print(f"{k} -> {v}")

def kill_spaces(encrypted_text, space):
    return "".join(space if ch == ' ' else ch for ch in encrypted_text)

def kill_doubles(encrypted_text, double):
    checked = ''
    memory = ''
    for ch in encrypted_text:
        if ch == memory:
            checked += double
            memory = double
        else:
            checked += ch
            memory = ch
    return checked

def main():
    text = input("Enter text to encrypt: ")
    difficulty = int(input("Enter difficulty 1-3: "))
    cipher = generate_substitution()
    cleaned_text = clean_text(text)    
    encrypted_text = encrypt(cleaned_text, cipher)
    space = cipher.get('-')
    double = cipher.get('+')
    
    if difficulty > 1:
        encrypted_text = kill_spaces(encrypted_text, space)
    if difficulty > 2:
        encrypted_text = kill_doubles(encrypted_text, double)
    
    print("Encrypted text:", encrypted_text)
    
    see_map = input('Do you want to check the cipher? y/n: ').lower()
    if see_map == 'y':
        print_mapping(cipher)

if __name__ == "__main__":
    main()
