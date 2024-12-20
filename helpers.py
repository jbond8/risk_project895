import sys

def is_near_target(x, target = 0.0, precision = .001):
    """checks to see if x > target-precision and x < target+precision
    """
    if (x > target-precision and x < target+precision):
        return True
    else:
        return False

def input_number(prompt):
    """ gives user f"{prompt} or q quits:" and waits for input,
        if input is an integer then returns integer,
        if input is a float then returns float,
        if input == "q" or "Q" then exit code
    """
    need_input = True
    while (need_input):
        x = input(f"{prompt} (or q quits):")
        if x == "q" or x == "Q":
            print("User terminated session")
            sys.exit()          
        try:
            y = int(x)
            return y
        except ValueError:
            pass
        try:
            z = float(x)
            return z
        except ValueError:
            print(f"{x} is not a number")

def is_lottery(lottery):
    """ returns true if lottery probabilities sum to near 1 and are all non-negative,
        lottery = [event-1, ..., event-n]
                   event-k = {"out": float_value, "prob": float_value}
    """
    total_prob = 0.0
    for event in lottery:
        if event['prob'] < 0.0: return False  #TODO fix for precision error
        total_prob += event['prob']
    if is_near_target(total_prob, target = 1, precision = .000001):
        return True
    else:
        return False

#if __name__ == "__main__":
    lottery = [{'out': 25.0, 'prob': 0.9553673849996607},
               {'out': 59.0, 'prob': 0.044632615000339326}]
    print(is_lottery(lottery))