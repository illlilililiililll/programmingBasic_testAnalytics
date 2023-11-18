import sys
import csv
input = sys.stdin.readline

total = []
title = input().strip()
input()

total_score = [0, 0, 0, 0, 0]
while 1:
    line = input().strip()
    if not line:
        break
    try:
        answer = int(line.split()[1])
        score = float(line.split()[2])
        total.append(answer)
        total_score[answer-1] += score
    except ValueError:
        total.append(0)

with open('answer.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # writer.writerow(['Subject', '1', 'Score1', '2', 'Score2', '3', 'Score3', '4', 'Score4', '5', 'Score5', 'Double Choice', 'Total'])
    line = [title]
    for i in range(1, 6):
        line.extend([(str(total.count(i)))+f'({round(total.count(i)/len(total)*100, 1)}%)', round(total_score[i-1], 1)])
    line.extend([(str(total.count(0)))+f'({round(total.count(0)/len(total)*100, 1)}%)', len(total)])
    writer.writerow(line)