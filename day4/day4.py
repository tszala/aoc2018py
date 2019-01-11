import sys
import os
import re
from collections import defaultdict
from datetime import datetime
from datetime import timedelta
from itertools import groupby

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\common'))

from fileutils import FileReader

pattern=re.compile(r'^\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\].*$')
guard_number_pattern=re.compile(r'^.+] Guard #(\d+).*$')

def guard_number(text):
    m=guard_number_pattern.match(text)
    if m == None:
        return None
    else:
        return int(m.groups()[0])

def parse_time_info(text):
    m=pattern.match(text)
    return datetime(int(m.groups()[0]),int(m.groups()[1]),int(m.groups()[2]),int(m.groups()[3]),int(m.groups()[4]))

def line_to_action(line):
    if 'falls asleep' in line:
        return 'SLEEP'
    elif 'wakes up' in line:
        return 'START SHIFT'
    else:
        return 'STOP SHIFT'

def group_shifts_to_guards(sorted_input):
    guard_shifts=defaultdict(list)
    guard=None
    for line in sorted_input:
        new_guard=guard_number(line)
        if guard == None:
            guard_shifts[new_guard].append((parse_time_info(line),'START SHIFT'))
            guard=new_guard
        else:
            if new_guard != None:
                guard_shifts[guard].append((parse_time_info(line),'STOP SHIFT'))
                guard_shifts[new_guard].append((parse_time_info(line),'START SHIFT'))
                guard=new_guard
            else:
                guard_shifts[guard].append((parse_time_info(line),line_to_action(line)))
    return guard_shifts

def count_sleep_time(shift_entries):
    seconds = 0
    for i in range(len(shift_entries)-1):
        entry=shift_entries[i]
        next_entry=shift_entries[i+1]
        if 'SLEEP' == entry[1]:
            seconds += (next_entry[0]-entry[0]).seconds
    return seconds/60

def get_minutes_between_dates(d1,d2):
    minutes=[]
    minute=timedelta(seconds=60)
    while d1 < d2:
        minutes.append(d1.minute)
        d1 += minute

    return minutes

def get_sleeping_minutes(shift_entries):
    sleeping_minutes=[]
    for i in range(len(shift_entries)-1):
        entry=shift_entries[i]
        next_entry=shift_entries[i+1]
        if 'SLEEP' == entry[1]:
            sleeping_minutes.append(get_minutes_between_dates(entry[0], next_entry[0]))
    return sleeping_minutes

def flatten_sleeping_minutes(sleeping_minutes):
    return [x for y in sleeping_minutes for x in y]

def group_sleeping_minutes(flat_sleeping_minutes):
    return {k:len(list(group)) for k, group in groupby(sorted(flat_sleeping_minutes))}

def sort_sleeping_minutes(grouped_sleeping_minutes):
    return sorted(grouped_sleeping_minutes.items(), key = lambda x: x[1], reverse=True)

#class Guard:
#    __init__(self, number, )

if __name__ == "__main__":
    print("Advent of Code day 4")
    f = FileReader()
    input = f.readFile("input.txt")
    print("Read %s lines of input" % len(input))
    shifts = group_shifts_to_guards(sorted(input))
    guards_with_sleep = [(guard,count_sleep_time(shift_entries)) for guard, shift_entries in shifts.items()]

    most_sleeping_guard=sorted(guards_with_sleep,key=lambda x: x[1], reverse=True)[0]
    print("The most sleeping guard is %i" % most_sleeping_guard[0])
    #print(shifts[most_sleeping_guard[0]])
    sleeping_minutes=[x for y in get_sleeping_minutes(shifts[most_sleeping_guard[0]]) for x in y]

    grouped_minutes={k:len(list(group)) for k, group in groupby(sorted(sleeping_minutes))}
    most_sleeping_minute=sorted(grouped_minutes.items(), key = lambda x: x[1], reverse=True)[0]
    print("Part 1 answer is ",(most_sleeping_guard[0] * most_sleeping_minute[0]))

    print("Part 2")

    guards_with_their_sleeping_minutes = {guard_no:sort_sleeping_minutes(group_sleeping_minutes(flatten_sleeping_minutes(get_sleeping_minutes(shifts_per_guard)))) for guard_no, shifts_per_guard in shifts.items()}
    v={k:v for k, v in guards_with_their_sleeping_minutes.items() if len(v) > 0}
    partTwoResult = sorted(v.items(), key=lambda x: x[1][0][1], reverse=True)[0]
    print(partTwoResult)
    print(partTwoResult[0] * partTwoResult[1][0][0])
