import re
import inspect


def ReplaceThreeOrMore(s):
    # pattern to look for three or more repetitions of any character, including
    # newlines.
    # pattern = re.compile(r"([aeioyu])\1{2,}", re.DOTALL) 
    pattern = re.compile(r"([aeioyu])\1{2}") 
    return pattern.sub(r"\1", s)

def RemoveVowAfterCon(s): 
    pattern = re.compile(r'(?<=[b-df-hj-np-tv-xz])[aeioyu]')
    # print (re.findall(pattern, s))
    return pattern.sub(r'', s)

def translate(phrase):
    
    pre_deal = RemoveVowAfterCon(phrase)
    print (pre_deal)
    pre_deal = ReplaceThreeOrMore(pre_deal)

    print (pre_deal)
    return pre_deal

def find_the_secret(f):
    res_ls = re.findall('[\w]+', f)
    res = ''.join(res_ls)
    
    return res    

def turn_2_str(ls_num):
    res = [str(i) for i in ls_num]
    return ''.join(res)
def create_phone_number(n):
    
    return '({first_3}) {mid}-{last}'.format(first_3 = turn_2_str(n[:3]), mid = turn_2_str(n[3:6]), last = turn_2_str(n[6:]))
    
if __name__ == '__main__': 
    # assert translate("hieeelalaooo") == "hello", "Hi!"
    # assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    # assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    # assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    # print("Coding complete? Click 'Check' to review your tests and earn   cool rewards!")
    
    # a = "hieeelalaooo"
    # print (find_the_secret(a))
    

    print (create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))