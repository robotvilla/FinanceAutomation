import csv

spendings = 0
earnings = 0
statements = []

with open('statements.CSV') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        row = row[:-1]
        row.pop(0)
        row.pop(3)

        #remove trailing element if it is empty
        while not row[-1]:
            row.pop()
        statements.append(row)
    
    print(statements[0])
    statements.pop(0)
    for statement in statements:
        print(statement)

        spending_or_earning = float(statement[2])
        if spending_or_earning < 0:
            spendings = spendings + spending_or_earning
        elif spending_or_earning > 0:
            earnings = earnings + spending_or_earning

    print("Spending: {0:.2f}".format(spendings))
    print("Earnings: {0:.2f}".format(earnings))