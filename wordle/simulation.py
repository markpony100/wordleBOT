import sys
sys.path.append('../data')
from answer import dictionary #real_w
from wordle import rand_select ,word_compare,end_game
from scipy.stats import entropy
import pandas as pd
import random
import time
def word_compare_1d(target,w_lst):
    '''word compare word to all words'''
    re_lst=[]
    for word in w_lst:
        re_lst.append(word_compare(target,word))
    return re_lst

def gen_table(w_lst1,w_lst2):
    '''
    gen lst1*lst2 table

    '''
    word_table={}
    for w1 in w_lst1:
        word_table[w1] = word_compare_1d(w1,w_lst2)
    return word_table

def best_entropy(table,step=0):
    best = -1
    best_w =''

    for idx,key in enumerate(table):
        entro_score = entropy(table[key].value_counts().values/len(table),base=2)
        if entro_score>best:
            best = entro_score
            best_w = key
    #print("best word: {}, score: {}".format(best_w,best))
    return best_w
def best_entropies(table,step=0):
    best_dic={}
    for idx,key in enumerate(table):
        entro_score = entropy(table[key].value_counts().values/len(table),base=2)
        best_dic[key]=entro_score
    return {k: v for k, v in sorted(best_dic.items(),reverse=True, key=lambda item: item[1])}

def sub_table(table, guess_w, row_idx, answer):
    sub_s = table[guess_w] 
    hint = word_compare(guess_w,answer)
    match_s = (sub_s[sub_s == hint])#matched rows in series
    cand = table.columns[match_s.index]# candidates in list
    re_table = table[cand].iloc[list(match_s.index)]
    return re_table.reset_index(drop=True)

def guess(table,row_idx,step=0):
    '''
    step 0 -> find best entropy within raw table
    step > find best entropy within filtered table
    n*m tabel
    n -> pos_w (table.column)
    m -> real_w
    '''
    guess_w = best_entropy(table)
    re_table = sub_table(table,guess_w,row_idx,ans)

    return re_table

if __name__ == "__main__":
    real_W = sorted(dictionary)#real answers
    pos_W =  sorted(dictionary)#possible answers
    ans = "biddy"
    condition = False
    table =  pd.DataFrame(gen_table(real_W,real_W))
    while(condition==False):
        guess = best_entropy(table)
        table = sub_table(table,guess,real_W,ans)
        #print(len(t))
        hint = word_compare(guess,ans)
        print("guess: ",guess)
        print("hint: ",hint)
        condition = end_game(hint)
