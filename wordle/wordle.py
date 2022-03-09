import sys
sys.path.append('../data')
from answer import dictionary #real_w
import random
real_w = sorted(dictionary)
pos_w =  sorted(dictionary)
def rand_select(real_w):
    return random.choice(real_w)
def letter_count(word):
    '''couting words return dict'''
    return {elem:word.count(elem) for elem in set(word)}
def guess_valid(word,dic):
    return word in dic
def guess(dic):
    condition = False
    while(condition==False):
        re = input("enter your guess: ")
        condition = guess_valid(re,dic)
        if not condition:
            print("Invalid guess")
    return re
def word_compare(guess,target):
    '''
    2 step check, word counting check then position check
    '''
    target_count = letter_count(target)
    re =""
    for idx,elem in enumerate(guess):
        if elem == target[idx]:#position and word match
            re+="2"
        elif elem in target_count.keys() and target_count[elem]>0:#word match
            target_count[elem]-=1
            re+="1"         
        else: re+="0"#no match
    return re
def end_game(result):
    if len(set(result))==1 and result[0]=="2":
        #print("game ends!")
        return True
    return False


if __name__ =="__main__":
    condition = False
    ans = rand_select(real_w)
    print("wordle answer :",ans)
    while(condition==False):
        gue = guess(pos_w)
        hint = word_compare(gue,ans)
        print(hint)
        condition = end_game(hint)




