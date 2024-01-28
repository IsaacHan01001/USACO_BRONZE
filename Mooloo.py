import datetime
now = datetime.datetime.now()

N, K = 5, 4 #map(int, input().split())
days = [7, 9, 13, 17, 21] #[x for x in list(map(int, input().split()))]
cost_foo = lambda x: x + K

continuous_cost = cost_foo(end - start + 1)
discrete_cost = 2*cost_foo(1)

Moonies = 0
ind = 0
previous_day = days[ind]

for day in days[1:]:
    next_day = day
    date_gap = next_day - previous_day + 1

    cost_individual = 2 * cost_foo(1)
    cost_together = cost_foo(date_gap)

    if cost_individual > cost_together:
        temp_cost = cost_together
    else:
        temp_cost = cost_individual

    temp_cost = cost_individual if cost_individual < cost_together else cost_together


    previous_day = day
    Moonies += temp_cost

print(Moonies)


end = datetime.datetime.now()


print('total run time: ', end - now)