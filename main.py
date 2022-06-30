#to calculate factorials 
def factorial(num):
    num = abs(round(num))
    if num>0:
        for i in range(1, num):
            num *= i
        return num
    elif num == 0:
        return 1

#variables
mcq_num = 20
cor_ans_per_mcq = 1 #if there are 4 options per mcq,1 is correct option(usually)
wrg_ans_per_mcq = 3 #if there are 4 options per mcq,3 are wrong options(usually)
min_cor_ans = 8

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
