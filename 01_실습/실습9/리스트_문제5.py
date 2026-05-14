price_table = [
    [8000,  9000,  8000],
    [13000, 15000, 13000],
    [10000, 12000, 10000],
]
seats = []
for i in range(5):
    seats.append(input())
prices = []

for seat in seats:
    row = seat[0]
    col = int(seat[1:])

    if row in 'ABCD':
        row_zone = 0
    elif row in 'EFGH':
        row_zone = 1
    else:
        row_zone = 2

    if col <= 3:
        col_zone = 0
    elif col <= 7:
        col_zone = 1
    else:
        col_zone = 2

    prices.append(price_table[row_zone][col_zone])

print(seats[prices.index(min(prices))])
