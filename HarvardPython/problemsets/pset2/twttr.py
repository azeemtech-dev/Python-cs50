'''vowels = ["a","A", "e","E", "i","I", "o","O", "u","U"]
result =""

inputs = input("Input: ")
for char in inputs:
    if char not in  vowels:
        result += char

print(f"Output: {result}")
'''
def main():
    user_input = input("input: ")
    print(f"Output: {remove_vowel(user_input)}")



def remove_vowel(text):
    vowel =  ["a","A", "e","E", "i","I", "o","O", "u","U"]
    result = ""

    for char in text:
        if char not in vowel:
            result += char
    return result

if __name__=="__main__":  
    main()

