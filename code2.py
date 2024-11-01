def GymPlan(v):
    """
    Я хочу в спортзал. Ціна одного відвідування 25$. Я можу купити п'ять візитів наперед
як один пакет за 18 доларів США за відвідування. Або я можу купити членську картку за 100 доларів і отримати
знижка 40% за кожне відвідування від початкової ціни в 25 доларів США. Напишіть функцію, яка приймає як
введіть ціле число, що представляє кількість відвідувань, запланованих на місяць, і повертає
рекомендація щодо того, який план використовувати («оплата за відвідування», «пакет на 5 відвідувань»,
«членство») у вигляді рядка.
    """
    p = v * 25
    f = v // 5
    t = f * 5 * 18
    c = 100 + v * 25 * 0.6
    
    if p < t and p < c:
        return "pay per visit"
    elif t < p and t < c:
        return "5-visit package"
    else:
        return 'membership'


print(GymPlan(65))