import random
import datetime
from scripts import sort_insertion, sort_selection, sort_merge

print("Generating lists...")
ran0 = random.sample(range(0, 100), 100)
ran1 = random.sample(range(0, 1000), 1000)
ran2 = random.sample(range(0, 10000), 10000)

def test(f):
    print("Testing", str(f))
    results = {'s0':None, 's1':None, 's2':None}
    time_start = datetime.datetime.now()
    f(ran0)
    results['s0'] = (datetime.datetime.now() - time_start).microseconds/1000
    time_start = datetime.datetime.now()
    f(ran1)
    results['s1'] = (datetime.datetime.now() - time_start).microseconds/1000
    time_start = datetime.datetime.now()
    f(ran2)
    results['s2'] = (datetime.datetime.now() - time_start).microseconds/1000
    return results

timings = {
    'sort_selection': test(sort_selection.selection_sort),
    'sort_insertion': test(sort_insertion.insertion_sort),
    'sort_merge': test(sort_merge.merge_sort)
}
print(timings)