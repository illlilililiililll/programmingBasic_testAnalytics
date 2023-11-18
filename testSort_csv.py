import sys
import csv
input = sys.stdin.readline

total = []
total_score = [0, 0, 0, 0, 0]
title = input().strip().split()
title = ' '.join(title[title.index(':')+1:title.index('과목코드')][:])
title = title[:title.index('(')]
while 1:
    _ = input().strip()
    if _ == '구분':
        break
    pass

while 1:
    line = input().strip()
    if not line:
        break
    elif not line[0].isdigit():
        continue
    
    try:
        answer = int(line.split()[2])
        total.append(answer)
        score = float(line.split()[1])
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