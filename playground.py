# Масти: трефы(clubs, C), пики(spades, S), червы(hearts, H), бубны(diamonds, D)
# Ранги: 2, 3, 4, 5, 6, 7, 8, 9, 10 (ten, T), валет (jack, J), дама (queen, Q), король (king, K), туз (ace, A)
# Например: AS - туз пик (ace of spades), TH - дестяка черв (ten of hearts), 3C - тройка треф (three of clubs)

import itertools
import random
import collections


def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
       s_nums = []
       m_nums = []
       e_nums = []
       for n in nums:
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       return quicksort(s_nums) + e_nums + quicksort(m_nums)

def straight(hand):
    """Возвращает True, если отсортированные ранги формируют последовательность 5ти,
    где у 5ти карт ранги идут по порядку (стрит)"""
    r = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    print(hand)


    



def card_ranks(hand):
    """Возвращает список рангов (его числовой эквивалент),
    отсортированный от большего к меньшему"""
    sorted_hand = []
    
    rangs = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    for i in hand:
        if i[0].isdigit():
            sorted_hand.append(int(i[0]))
        for j in rangs.keys():
            if i[0] == j:
                sorted_hand.append(rangs.get(j))
                
                
    
    result = quicksort(sorted_hand)
    return result

def flush(hand:list) -> bool:
    #print(hand)
    """Возвращает True, если все карты одной масти"""
    res_1 = filter(lambda x: 'C' in x, hand)
    res_2 = filter(lambda x: 'S' in x, hand)
    res_3 = filter(lambda x: 'H' in x, hand)
    res_4 = filter(lambda x: 'D' in x, hand)

    check_C = len(list(res_1))
    check_S = len(list(res_2))
    check_H = len(list(res_3))
    check_D = len(list(res_4))

    if (check_C or check_S or check_H or check_D) == 7:
        print('Yep')
        return True
    return False

def straight(ranks):
    """Возвращает True, если отсортированные ранги формируют последовательность 5ти,
    где у 5ти карт ранги идут по порядку (стрит)"""
    count = 0

    for i in range(len(ranks)-1):
        if ranks[i] + 1 == ranks[i+1]:
            count+=1

    #print(count)
    if count == 5:
        return True
    return False

def kind(n, ranks):
    """Возвращает первый ранг, который n раз встречается в данной руке.
    Возвращает None, если ничего не найдено"""
    n_table = collections.Counter(ranks)
    res = n_table.get(n)
    print(n_table)
    for key, value in n_table.items():
        if value == n:
            return key
    return None

if __name__ == '__main__':
    hand_1 = "6C 7C 8C 9C TC 5C 7B".split()
    hand_2 = 'JD TD TS 7D 8D TB 3D'.split()
    hand_3 = "6C 7C 8C 9C TC 5C AC".split()
    hand_4 = "TD TC 5H 5C 7C kR AB".split()
    hand_5 = "AD AC AH 5C 7C kR AB".split()
    #print(*hand)
    #print(flush(hand_2))
    s = card_ranks(hand_5)
    print(s)

    straight(s)
    print(kind(4, s))

    
