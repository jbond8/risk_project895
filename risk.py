import helpers as hlpr
import lottery as lot
import utility_functions as uf
import agent
import random
import matplotlib.pyplot as plt

def stepwise_elict(money_min = 0, money_max = 100, utilfn = uf.linear_utility):

    xp = [money_min,money_max]
    fp = [money_min,money_max]

    lottery_ce1 = [{'out': money_min, 'prob': 0.5}, {'out': money_max, 'prob': 0.5}]
    print(f"\n The lottery has a 50/50 probability that it will either pay out {lottery_ce1[0].get('out')} or {lottery_ce1[1].get('out')}")

    ce_1 = float(input("\n If I offered you a guaranteed amount of money"
                 "instead of the chance to win this lottery,"
                 "how much would you need for you to be just as happy"
                 "with the guaranteed money as you are with the lottery?: "))
    ev_1 = agent.expected_value(lottery_ce1)
    xp.append(ce_1)
    fp.append(ev_1)
    print(f"\n ev_1,ce_1 of lottery is {ev_1},{ce_1}")

    lottery_ce2 = [{'out': money_min, 'prob': 0.5}, {'out': ce_1, 'prob': 0.5}]
    print(f"\n The lottery has a 50/50 probability that it will either pay out {lottery_ce2[0].get('out')} or {lottery_ce2[1].get('out')}")
    ce_2 = float(input("\n If I offered you a guaranteed amount of money"
                 "instead of the chance to win this lottery,"
                 "how much would you need for you to be just as happy"
                 "with the guaranteed money as you are with the lottery?: "))
    ev_2 = agent.expected_value(lottery_ce2)
    xp.append(ce_2)
    fp.append(ev_2)
    print(f"ev_1,ce_1 of lottery is {ev_2},{ce_2}")

    lottery_ce3 = [{'out': ce_1, 'prob': 0.5}, {'out': money_max, 'prob': 0.5}]
    print(f"\n The lottery has a 50/50 probability that it will either pay out {lottery_ce3[0].get('out')} or {lottery_ce3[1].get('out')}")
    ce_3 = float(input("\n If I offered you a guaranteed amount of money"
                 "instead of the chance to win this lottery,"
                 "how much would you need for you to be just as happy"
                 "with the guaranteed money as you are with the lottery?: "))
    ev_3 = agent.expected_value(lottery_ce3)
    xp.append(ce_3)
    fp.append(ev_3)
    print(f"ev_1,ce_1 of lottery is {ev_3},{ce_3}")

    
    events_n = int(input("How many events would you like to run?: "))
    for i in range(events_n):
        RanMin = random.randrange(money_min,money_max)
        RanMax = random.randrange(money_min, money_max)
        while RanMax < RanMin:
            RanMax = random.randrange(money_min, money_max)
        lottery_cen = [{'out': RanMin, 'prob': 0.5}, {'out': RanMax, 'prob': 0.5}]
        print(lottery_cen[0])
        print(f"\n The lottery has a 50/50 probability that it will either pay out {lottery_cen[0].get('out')} or {lottery_cen[1].get('out')}")
        ce_n = float(input("\n If I offered you a guaranteed amount of money"
                 "instead of the chance to win this lottery,"
                 "how much would you need for you to be just as happy"
                 "with the guaranteed money as you are with the lottery?: "))
        ev_n = agent.expected_value(lottery_cen)
        print(f"\n expected value and certainty equivalent of lottery {i} is {ev_n},{ce_n}")
        xp.append(ev_n)
        fp.append(ce_n)

    xp.sort()
    fp.sort()

    print(xp)
    print(fp)

    slope_list = [(fp[i+1] - fp[i]) / (xp[i+1] - xp[i]) for i in range(len(xp) - 1)]

    piecewise_list = [[{'slope': slope_list[x], 'intercept': fp[x], 'x_min': xp[x], 'x_max': xp[x+1]}] for x in range(len(xp) - 1)]
    
    print("\n The Piecewise Functions:")
    for subdomain in range(len(piecewise_list)):
        print(f"{piecewise_list[subdomain][0].get('slope')}x, if {piecewise_list[subdomain][0].get('x_min')} ≤ x ≤ {piecewise_list[subdomain][0].get('x_max')}")

stepwise_elict()