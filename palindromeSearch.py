def palindrome(sentence):
    for i in (",.'?/><}{{}}'"):
        sentence = sentence.replace(i," ")
    palindrome = []
    words = sentence.split()
    for word in words:
        word = word.lower()
        if word == word[::-1]:
            palindrome.append(word)
    return palindrome


if __name__ == "__main__":
    result = palindrome("LOL, my interview went good. My mom will be so happy.")
    print(result)