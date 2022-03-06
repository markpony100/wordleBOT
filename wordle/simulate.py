import sys
sys.path.append('../data')
from answer import dictionary #real_w
from wordle import rand_select,word_compare
import pandas as pd
import random
real_w = sorted(dictionary)
pos_w =  sorted(dictionary)

def word_compare_1d(target,w_lst):
    '''word compare word to all words'''
    re_lst=[]
    for word in w_lst:
        re_lst.append(word_compare(target,word))
    return re_lst

def gen_table(w_lst1,w_lst2):
    '''gen lst2lst table'''
    word_table={}
    for w1 in w_lst1:
        word_table[w1] = word_compare_1d(w1,w_lst2)
    return word_table

if __name__ == "__main__":
    table =  pd.DataFrame(gen_table(real_w,real_w))
    ans = rand_select(real_w)
    guess = []
    guess.append(rand_select(real_w))
    sub_s = table[guess[-1]]
    print(sub_s[sub_s == word_compare(guess[-1],ans)])
