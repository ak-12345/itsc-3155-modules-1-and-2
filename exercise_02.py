def suffix(words1, words2):
    if words1.endswith(words2) or words2.endwith(words1):
        print("True")
    else:
        print("False")
words1 = input('Word 1: ')
words2 = input('Word 2: ')
suffix(words1,words2)
