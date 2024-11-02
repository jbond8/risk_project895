import helpers as hlpr
import lottery as lot
import utility_functions as uf
import agent
import holt_laury as hl
import random
import matplotlib.pyplot as plt

def input_stepwise_elict(money_min = 0, money_max = 100):

    xp = [money_min,money_max]
    fp = [money_min,money_max]
    lottery_ce1 = [{'out': money_min, 'prob': 0.5}, {'out': money_max, 'prob': 0.5}]
    print(f"\n The lottery has a 50/50 probability that it will either pay out {lottery_ce1[0].get('out')} or {lottery_ce1[1].get('out')}")

    ce_1 = float(input("\nIf I offered you a guaranteed amount of money"
                 " instead of the chance to win this lottery,"
                 " how much would you need for you to be just as happy"
                 " with the guaranteed money as you are with the lottery?: "))
    ev_1 = agent.expected_value(lottery_ce1)
    xp.append(ev_1)
    fp.append(ce_1)
    print(f"\n ev_1,ce_1 of lottery is {ev_1},{ce_1}")

    lottery_ce2 = [{'out': money_min, 'prob': 0.5}, {'out': ce_1, 'prob': 0.5}]
    print(f"\n The lottery has a 50/50 probability that it will either pay out {lottery_ce2[0].get('out')} or {lottery_ce2[1].get('out')}")
    ce_2 = float(input("\nIf I offered you a guaranteed amount of money"
                 " instead of the chance to win this lottery,"
                 " how much would you need for you to be just as happy"
                 " with the guaranteed money as you are with the lottery?: "))
    ev_2 = agent.expected_value(lottery_ce2)
    xp.append(ev_2)
    fp.append(ce_2)
    print(f"ev_1,ce_1 of lottery is {ev_2},{ce_2}")

    lottery_ce3 = [{'out': ce_1, 'prob': 0.5}, {'out': money_max, 'prob': 0.5}]
    print(f"\n The lottery has a 50/50 probability that it will either pay out {lottery_ce3[0].get('out')} or {lottery_ce3[1].get('out')}")
    ce_3 = float(input("\nIf I offered you a guaranteed amount of money"
                 " instead of the chance to win this lottery,"
                 " how much would you need for you to be just as happy"
                 " with the guaranteed money as you are with the lottery?: "))
    ev_3 = agent.expected_value(lottery_ce3)
    xp.append(ev_3)
    fp.append(ce_3)
    print(f"ev_1,ce_1 of lottery is {ev_3},{ce_3}")

    
    events_n = int(input("How many events would you like to run?: "))
    if events_n < 0:
        print()
        events_n = int(input("Negative numbers not accepted!\n How many events would you like to run?: "))
    else:
        for i in range(events_n):
            RanMin = random.randrange(money_min,money_max)
            RanMax = random.randrange(money_min, money_max)
            while RanMax < RanMin:
                RanMax = random.randrange(money_min, money_max)
            lottery_cen = [{'out': RanMin, 'prob': 0.5}, {'out': RanMax, 'prob': 0.5}]
            print(lottery_cen[0])
            print(f"\nThe lottery has a 50/50 probability that it will either pay out {lottery_cen[0].get('out')} or {lottery_cen[1].get('out')}")
            ce_n = float(input("\nIf I offered you a guaranteed amount of money"
                 " instead of the chance to win this lottery,"
                 " how much would you need for you to be just as happy"
                 " with the guaranteed money as you are with the lottery?: "))
            ev_n = agent.expected_value(lottery_cen)
            print(f"\n expected value and certainty equivalent of lottery {i} is {ev_n},{ce_n}")
            xp.append(ev_n)
            fp.append(ce_n)

    xp.sort()
    fp.sort()

    slope_list = [(fp[i+1] - fp[i]) / (xp[i+1] - xp[i]) for i in range(len(xp) - 1)]
    print(slope_list)
    intercept_list = [(slope_list[i]*(xp[0] - xp[i]) + fp[i]) for i in range(len(slope_list))]

    piecewise_list = [[{'slope': slope_list[x], 'intercept': intercept_list[x], 'x_min': xp[x], 'x_max': xp[x+1]}] for x in range(len(xp) - 1)]
    
    print(piecewise_list)

    print("\nThe Piecewise Functions (intercept, slope, conditions):")
    print('---------------------------')
    print(f"{piecewise_list[0][0].get('intercept')}, {piecewise_list[0][0].get('slope')}x, if {piecewise_list[0][0].get('x_min')} ≤ x ≤ {piecewise_list[0][0].get('x_max')}")
    for subdomain in range(len(piecewise_list) - 1):
        print(f"{piecewise_list[subdomain+1][0].get('intercept')}, {piecewise_list[subdomain+1][0].get('slope')}x, if {piecewise_list[subdomain+1][0].get('x_min')} < x ≤ {piecewise_list[subdomain+1][0].get('x_max')}")

    return piecewise_list

def auto_stepwise_elict(money_min = 0, money_max = 100, utilfn = uf.linear_utility, events_n = 0):
    
    xp = [money_min,money_max]
    fp = [money_min,money_max]

    lottery_ce1 = [{'out': money_min, 'prob': 0.5}, {'out': money_max, 'prob': 0.5}]
    print(f"\n The lottery has a 50/50 probability that it will either pay out {lottery_ce1[0].get('out')} or {lottery_ce1[1].get('out')}")

    ce_1 = agent.expected_utility(lottery_ce1, utilfn)
    ev_1 = agent.expected_value(lottery_ce1)
    xp.append(ev_1)
    fp.append(ce_1)
    print(f"\n ev_1,ce_1 of lottery is {ev_1},{ce_1}")

    lottery_ce2 = [{'out': money_min, 'prob': 0.5}, {'out': ce_1, 'prob': 0.5}]
    print(f"\n The lottery has a 50/50 probability that it will either pay out {lottery_ce2[0].get('out')} or {lottery_ce2[1].get('out')}")
    ce_2 = agent.expected_utility(lottery_ce2, utilfn)
    ev_2 = agent.expected_value(lottery_ce2)
    xp.append(ev_2)
    fp.append(ce_2)
    print(f"ev_1,ce_1 of lottery is {ev_2},{ce_2}")

    lottery_ce3 = [{'out': ce_1, 'prob': 0.5}, {'out': money_max, 'prob': 0.5}]
    print(f"\n The lottery has a 50/50 probability that it will either pay out {lottery_ce3[0].get('out')} or {lottery_ce3[1].get('out')}")
    ce_3 = agent.expected_utility(lottery_ce3, utilfn)
    ev_3 = agent.expected_value(lottery_ce3)
    xp.append(ev_3)
    fp.append(ce_3)
    print(f"ev_1,ce_1 of lottery is {ev_3},{ce_3}")

    if events_n < 0:
        print()
        events_n = int(input("Negative numbers not accepted!\n How many events would you like to run?: "))
    else:
        for i in range(events_n):
            RanMin = random.randrange(money_min,money_max)
            RanMax = random.randrange(money_min, money_max)
            while RanMax < RanMin:
                RanMax = random.randrange(money_min, money_max)
            lottery_cen = [{'out': RanMin, 'prob': 0.5}, {'out': RanMax, 'prob': 0.5}]
            print(lottery_cen[0])
            print(f"\nThe lottery has a 50/50 probability that it will either pay out {lottery_cen[0].get('out')} or {lottery_cen[1].get('out')}")
            ce_n = agent.expected_utility(lottery_cen, utilfn)
            ev_n = agent.expected_value(lottery_cen)
            print(f"\n expected value and certainty equivalent of lottery {i} is {ev_n},{ce_n}")
            xp.append(ev_n)
            fp.append(ce_n)

    xp.sort()
    fp.sort()

    return xp, fp

def plot_utility(piecewise_list):

    x = []
    y = []

    for piece in range(len(piecewise_list)):
        for i in range(int(piecewise_list[piece][0].get('x_min') / 0.01), int(piecewise_list[piece][0].get('x_max') / 0.01)):
                x.append(i * 0.01)
                y.append(i * 0.01 * piecewise_list[piece][0].get('slope') + piecewise_list[piece][0].get('intercept'))
    
    plt.plot(x,y)
    plt.show()

def get_lottery_choices(holt_laury_lotteries, piecewise):
    lottery_choices = []
    for lottery_pair in holt_laury_lotteries:
        k = lottery_choice_step(lottery_pair, piecewise)[0]
        lottery_choices.append(k)
    return lottery_choices

def lottery_pair_eucalc(lottery_pair, piecewise):
    lottery_pair_eu = []
    for lottery in lottery_pair:
        eu = 0.0
        for event in lottery:
            out = event['out']
            for piece in piecewise:
                if out > piece[0].get('x_min') and out <= piece[0].get('x_max'):
                    eu += (piece[0].get("slope") * event['out'] + piece[0].get("intercept")) * event['prob']
        lottery_pair_eu.append(eu)
    return lottery_pair_eu

def lottery_choice_step(lottery_pair, piecewise):
    """ Choose the lottery with the highest expected utility
        from lottery_list using utility function u.
        
        returns:
            lottery_index, eu  expected utility of the lottery
    """
    lottery_index = None
    list_of_expected_u = []
    lottery_pair_utility = lottery_pair_eucalc(lottery_pair,piecewise)
    list_of_expected_u.append(lottery_pair_utility)
    choice = max(lottery_pair_utility)
    lottery_index = list_of_expected_u[0].index(choice)
    return lottery_index, choice
