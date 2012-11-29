import csv

input = open('card.csv', 'r')
output = open('clean.csv', 'w')
writer = csv.writer(output)
for row in csv.reader(input):
    if row:
        writer.writerow(row)
input.close()
output.close()
