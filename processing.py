def portions(num):
    return [num * 0.5,num * 0.3,num * 0.2]

def annualAmount(an, sav):
    data = []
    for i in range(0, 11):
        data.append(((an * 0.2) * i) + sav)
    return data


