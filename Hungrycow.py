def solve():
    N, T = map(int, input().split())

    delivery = []
    for i in range(N):
        delivery.append(list(map(int, input().split())))

    def update(ans, stock, day_right_now, d_date):
        date_gap = d_date - day_right_now
        if stock >= date_gap:
            ans += date_gap
            stock -= date_gap
        elif stock == 0:
            return ans, stock, d_date
        else:
            ans += stock
            stock = 0
        return ans, stock, d_date




    delivery_counter = 0
    stock = delivery[0][1]
    ans = 0
    day_right_now = delivery[0][0]

    for i in range(len(delivery) - 1):
        d_date = delivery[i + 1][0]
        ans, stock, day_right_now = update(ans, stock, day_right_now, d_date)
        stock += delivery[i + 1][1]

    #last update
    ans, stock, day_right_now = update(ans, stock, day_right_now, T + 1)
    print(ans)

if __name__ == "__main__":
    solve()

#
# for i in range(1, T + 1):
#     if delivery_counter < len(delivery):
#         if delivery[delivery_counter][0] == i:
#             stock += delivery[delivery_counter][1]
#             delivery_counter += 1
#     if stock > 0:
#         ans += 1
#         stock -= 1
