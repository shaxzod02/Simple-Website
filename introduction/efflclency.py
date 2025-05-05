import time
def efflclency_measure(fube, args):
    start_time = time.time()
    result = fube(*args)
    end_time = time.time()
    return [result, round(end_time-start_time, 2)]