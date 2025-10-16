


def average(arg_1, arg_2) ->float:
    return  arg_1 / arg_2 

def hot_day(arg):
    return sum(1 for t in arg if t > 25)
def cold_day(arg):
    return sum(1 for t in arg if t < 10 )
def analyze_temperature(temperatures):
    if not len(temperatures) == 7:
        return None
    elif len(temperatures) == 0:
        return  None
    else:
        get_sum = sum(temperatures)
        get_len = len(temperatures)
        average_temperatura = average(get_sum, get_len)
        
        result = {"average": round(average_temperatura,1),
            "min": min(temperatures),
            "max": max(temperatures),
            "hot_days": hot_day(temperatures),
            "cold_days": cold_day(temperatures),
            }
        
        return result