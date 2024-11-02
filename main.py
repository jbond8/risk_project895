from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import risk

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

session_store = []

def get_session():
    return session_store

utility_functions_map = {
    "linear_utility": risk.uf.linear_utility,
    "cara_utility":risk.uf.cara_utility,
    "crra_utility":risk.uf.crra_utility,
    "exp_utility":risk.uf.exponential_utility,
    "hara_utility":risk.uf.hara_utility
}

@app.get('/')
async def index(request:Request):
    return templates.TemplateResponse('index.html',context={'request':request,'id':id})

@app.get('inputstep')



@app.get("/autostep")
def auto_stepwise_elict(money_min = 0, money_max = 100, utilfn = "linear_utility", events_n = 0):
    """
    Runs an auto stepwise elicitation algorithim to build piecewise linear utility functions for a given utility function.
    
        args:
            money_min, minimum amount of money offered in a lottery
            money_max, maximum amount of money offered in a lottery
            utilfn, utility function which can be:
                linear_utility, Linear Utility
                cara_utility, Constant Absolute Risk Aversion
                crra_utility, Constant Relative Risk Aversion
                exp_utility, Exponential Utility
                hara_utility, Hyperbolic Absolute Risk Aversion

            events_n, number of additional lotteries to run the utility function through
        
        returns:
            piecewise_list, a list of linear piecewise functions as dictionaries containing:
                slope, slope of linear piecewise function
                intercept, intercept of linear piecewise function
                x_min, minimum x value of linear piecewise function
                x_max, maximum x value of lienar piecewise function
    
    """
    
    money_min = int(money_min)
    money_max = int(money_max)
    utilfn = utility_functions_map.get(utilfn)
    events_n = int(events_n)
    maxmoney_dupelot = [{'out': 0, 'prob': 0}, {'out': money_max, 'prob': 1}]

    xp = [money_min,money_max]
    fp = [money_min,risk.agent.expected_utility(maxmoney_dupelot,utilfn)]

    lottery_ce1 = [{'out': money_min, 'prob': 0.5}, {'out': money_max, 'prob': 0.5}]

    ce_1 = risk.agent.certainty_equivalent(lottery_ce1, utilfn, money_min, money_max, 0.01)[0]
    eu_1 = risk.agent.expected_utility(lottery_ce1, utilfn)
    xp.append(ce_1)
    fp.append(eu_1)

    lottery_ce2 = [{'out': money_min, 'prob': 0.5}, {'out': ce_1, 'prob': 0.5}]
    ce_2 = risk.agent.certainty_equivalent(lottery_ce2, utilfn, money_min, money_max, 0.01)[0]
    eu_2 = risk.agent.expected_utility(lottery_ce2, utilfn)
    xp.append(ce_2)
    fp.append(eu_2)

    lottery_ce3 = [{'out': ce_1, 'prob': 0.5}, {'out': money_max, 'prob': 0.5}]
    ce_3 = risk.agent.certainty_equivalent(lottery_ce3, utilfn, money_min, money_max, 0.01)[0]
    eu_3 = risk.agent.expected_utility(lottery_ce3, utilfn)
    xp.append(ce_3)
    fp.append(eu_3)

    n_loader = 0

    if int(events_n) < 0:
        print()
        print("Negative numbers not accepted!")
    else:
        while len(xp) -5 < events_n:
            RanMin = risk.random.randrange(money_min,money_max)
            RanMax = risk.random.randrange(money_min, money_max)
            while RanMax < RanMin:
                RanMax = risk.random.randrange(money_min, money_max)
            lottery_cen = [{'out': RanMin, 'prob': 0.5}, {'out': RanMax, 'prob': 0.5}]
            ce_n = risk.agent.certainty_equivalent(lottery_cen, utilfn, money_min, money_max, 0.01)[0]
            eu_n = risk.agent.expected_utility(lottery_cen, utilfn)
            if ce_n not in xp:
                xp.append(ce_n)
                fp.append(eu_n)

    xp.sort()
    fp.sort()

    slope_list = [(fp[i+1] - fp[i]) / (xp[i+1] - xp[i]) for i in range(len(xp) - 1)]
    intercept_list = [(slope_list[i]*(xp[0] - xp[i]) + fp[i]) for i in range(len(slope_list))]

    piecewise_list = [[{'slope': slope_list[x], 'intercept': intercept_list[x], 'x_min': xp[x], 'x_max': xp[x+1]}] for x in range(len(xp) - 1)]

    session_store.clear()
    session_store.extend(piecewise_list)

    return piecewise_list

@app.get("/holt_laury_piecewise")
def holt_laury_piecewise():
    util = get_session()
    holt_laury_lots = risk.hl.build_holt_laury_lotteries()
    choices = risk.get_lottery_choices(holt_laury_lots, util)
    return holt_laury_lots, choices