def print_HL_lottery(lottery):
    p1 = lottery[0]['prob']
    o1 = lottery[0]['out']
    p2 = lottery[1]['prob']
    o2 = lottery[1]['out']
    print(f"[{o1}]({p1}) : [{o2}]({p2})", end = "  ")   


def print_HL_lottery_pair(lottery_pair):
    first_lottery = lottery_pair[0]
    second_lottery = lottery_pair[1]
    print_HL_lottery(first_lottery)  
    print_HL_lottery(second_lottery)
    print()
    
def print_HL_lottery_pair_and_choice(lottery_pair, choice):
    first_lottery = lottery_pair[0]
    second_lottery = lottery_pair[1]
    print_HL_lottery(first_lottery)  
    if choice == 0:
        print("--A", end = " ")
        print_HL_lottery(second_lottery) 
        print()
    else:
        print("   ", end = " ")
        print_HL_lottery(second_lottery)
        print("--B")

        
def build_holt_laury_lotteries():
    """Returns list of Holt-Laury lottery pairs.
    
        returns:
            holt_laury_lotteries, list of lists
                inner list is a pair of lotteries for choice
    
    """
    #  Can we take advantage of the structure of lotteries in the Holt-Laury paper
    pay_a_high = 200*0.25974025974026
    pay_a_low = 160*0.25974025974026
    pay_b_high = 100
    pay_b_low =  10*0.25974025974026
    # Now we can build holt_laury_lotteries
    holt_laury_lotteries = []
    p = 0.0
    for k in range(9):
        p = round(p + 0.10, 2)
        lottery_a = [{'prob': p, 'out': pay_a_high}, {'prob': round(1.0-p, 2), 'out': pay_a_low}]
        lottery_b = [{'prob': p, 'out': pay_b_high}, {'prob': round(1.0-p, 2), 'out': pay_b_low}]
        holt_laury_lotteries.append([lottery_a, lottery_b])
    return holt_laury_lotteries