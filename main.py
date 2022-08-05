from factorial import factorial
from variables import *


def main():
    total_combs = 0
    for i in range(min_cor_ans, mcq_num+1):
        cor_ans_per_comb = i
        wrg_ans_per_comb = mcq_num - i
        num_of_combs = factorial(mcq_num)/(factorial(cor_ans_per_comb)*factorial(wrg_ans_per_comb))
        comb_amount_per_combs = (cor_ans_per_mcq**cor_ans_per_comb) * (wrg_ans_per_mcq**wrg_ans_per_comb)
        total_combs += num_of_combs * comb_amount_per_combs

    opt_per_mcq = cor_ans_per_mcq + wrg_ans_per_mcq
    prob = (total_combs*100/opt_per_mcq**mcq_num)
    print(f"Probability of having atleast {min_cor_ans} correct answer out of {mcq_num} is...\n  {prob}%")

main()
