"""
Τμήμα Πληροφορικής και Τηλεπικοινωνιών - Άρτα 
Πανεπιστήμιο Ιωαννίνων 

Γκόγκος Χρήστος 
http://chgogos.github.io/
Εαρινό εξάμηνο 2020-2021
"""

import sys
import os
import csv
import datetime as dt

def enter_exit(fn):
    file = open(fn, newline='', encoding="utf16")
    reader = csv.reader(file, delimiter="\t")
    header = next(reader)
    monitor = {}
    start_time = None
    finish_time = None
    for row in reader:
        name = row[0]
        status = None
        if row[1]== "Συμμετέχει":
            status="IN"
        elif row[1]== "Αποχώρησε":
            status="OUT"
        timestamp = dt.datetime.strptime(row[2], '%m/%d/%Y, %H:%M:%S %p')
        if start_time is None:
            start_time = timestamp
        if finish_time is None:
            finish_time = timestamp
        if start_time > timestamp:
            start_time = timestamp
        if finish_time < timestamp:
            finish_time = timestamp
        if name in monitor:
            monitor[name].append((status, timestamp))
        else:
            monitor[name] = [(status, timestamp)]
    file.close()
    duration = finish_time - start_time
    for name in monitor:
        total = 0
        status = None
        last_in = None
        connections = 0;
        for rec in monitor[name]:
            if rec[0]=='IN':
                status = "IN"
                last_in = rec[1]
                t1 = rec[1]
                connections += 1
            elif rec[0] == 'OUT':
                status = "OUT"
                total += (rec[1] - t1).total_seconds()
        if status == "IN":
            total += (finish_time - last_in).total_seconds()
        total_h_m_s = dt.timedelta(seconds=total)
        print(f'{name} {total_h_m_s} ΣΥΝΔΕΣΕΙΣ={connections}')

    print(f'Έναρξη={start_time} Λήξη={finish_time} Διάρκεια={duration}')
    print(f'Συμμετοχές= {len(monitor)}')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        enter_exit("20210225-lab-anonymized.csv")
    else:
        enter_exit(sys.argv[1])