# pangram

sentence = input ()

def is_pangram (sentence):
    sentence = set ( sentence.lower ().replace (" ", "") )
    alpha_counter = 0
    for char in sentence:
        if char.isalpha ():
            alpha_counter += 1
    return alpha_counter == 26

print (is_pangram (sentence))
    