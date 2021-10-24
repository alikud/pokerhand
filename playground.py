# Масти: трефы(clubs, C), пики(spades, S), червы(hearts, H), бубны(diamonds, D)
# Ранги: 2, 3, 4, 5, 6, 7, 8, 9, 10 (ten, T), валет (jack, J), дама (queen, Q), король (king, K), туз (ace, A)
# Например: AS - туз пик (ace of spades), TH - дестяка черв (ten of hearts), 3C - тройка треф (three of clubs)

import itertools
import random

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
    

    for i in hand:
        if i[0] == 'J':
            sorted_hand.append(11)
        if i[0] == 'T':
            sorted_hand.append(10)
        if i[0] == 'Q':
            sorted_hand.append(12)
        if i[0] == 'K':
            sorted_hand.append(13)
        if i[0] == 'A':
            sorted_hand.append(14)
        if i[0].isdigit():
            sorted_hand.append(int(i[0]))
    
    h = quicksort(sorted_hand)
    return h

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

if __name__ == '__main__':
    hand_1 = "6C 7C 8C 9C TC 5C 7B".split()
    hand_2 = 'JD TD TS 7D 8D TB 3D'.split()
    hand_3 = "6C 7C 8C 9C TC 5C ?C".split()
    hand_4 = "TD TC 5H 5C 7C ?R ?B".split()
    #print(*hand)
    #print(flush(hand_2))
    s = card_ranks(hand_2)
    print(s)

    
