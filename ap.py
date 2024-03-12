def maxliste(liste):
    max_val = 0
    for x in range (len(liste)):
        if liste [x] > max_val :
            max_val = liste[x]
        return max_val

assert maxliste([98,12,104,23,131,9])
assert maxliste([-27,24,-3,15])