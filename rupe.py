r = ['низкий', 'удовлетворительный', 'средний', 'выше среднего', 'высокий']
def experement(age, t1, t2, t3):
    res = (4*(t1+t2+t3)-200)/10
    txt_res = ''

    if age >= 15:
        if res >= 15:
            txt_res = r[0]
        elif res < 15 and res >= 11:
            txt_res = r[1]
        elif res < 11 and res >= 6:
            txt_res = r[2]
        elif res < 6 and res >= 0.5:
            txt_res = r[3]
        elif res < 0.5:
            txt_res = r[4]

    elif age >= 13:
        if res >= 16.5:
            txt_res = r[0]
        elif res < 16.5 and res >= 12.5:
            txt_res = r[1]
        elif res < 12.5 and res >= 7.5:
            txt_res = r[2]
        elif res < 7.5 and res >= 2:
            txt_res = r[3]
        elif res < 2:
            txt_res = r[4]

    elif age >= 12:
        if res >= 18:
            txt_res = r[0]
        elif res < 18 and res >= 14:
            txt_res = r[1]
        elif res < 14 and res >= 9:
            txt_res = r[2]
        elif res < 9 and res >= 3.5:
            txt_res = r[3]
        elif res < 3.5:
            txt_res = r[4]

    elif age >= 9:
        if res >= 19.5:
            txt_res = r[0]
        elif res < 19.5 and res >= 15.5:
            txt_res = r[1]
        elif res < 15.5 and res >= 10.5:
            txt_res = r[2]
        elif res < 10.5 and res >= 5:
            txt_res = r[3]
        elif res < 5:
            txt_res = r[4]
        
    elif age >= 7:
        if res >= 21:
            txt_res = r[0]
        elif res < 21 and res >= 17:
            txt_res = r[1]
        elif res < 17 and res >= 12:
            txt_res = r[2]
        elif res < 12 and res >= 6.5:
            txt_res = r[3]
        elif res < 6.5:
            txt_res = r[4]

    return res, txt_res 