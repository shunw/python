def show_alps(alp, bef_list, guess):
    for n, i in enumerate(guess): 
        if i == alp:
            bef_list[n] = alp
    return bef_list


guess = ['g', 'u', 'e', 's', 's']
bef_list = list('_'*len(guess))
print show_alps('s', bef_list, guess)
bef_list = show_alps('s', bef_list, guess)
print show_alps ('g', bef_list, guess)