

class User:
    def __init__(self, name, sex, age, height, health, fitness, finance):
        self.name = name
        self.sex = sex
        self.age = age
        self.height = height
        self.health = health
        self.fitness = fitness
        self.finance = finance



#f = fasted
#tt = total testosterone


class Health:
    def __init__(self, waist_circ, a1c, hdl, ldl, tg, fglucose, finsulin, vitd, tt, votwomax):
        self.waist_circ = waist_circ
        self.a1c = a1c
        self.hdl = hdl
        self.ldl = ldl
        self.tg = tg
        self.fglucose = fglucose
        self.finsulin = finsulin
        self.vitd = vitd
        self.tt = tt
        self.votwomax = votwomax

#bfp = body fat %
#dl = deadlift
#bpress = bench press
#wchinups = weighted chin ups
#dhang = dead hang

class Fitness:
    def __init__(self, weight, bfp, hundred_m, marathon, dl, squat, bpress, ohp, wchinups, dhang):
        self.weight = weight
        self.bfp = bfp
        self.hundred_m = hundred_m
        self.marathon = marathon
        self.dl = dl
        self.squat = squat
        self.bpress = bpress
        self.ohp = ohp
        self.wchinups = wchinups
        self.dhang = dhang

class Finance:
    def __init__(self, BTC, asset_value, monthly_income, monthly_expenditure, debt):
        self.BTC = BTC
        self.asset_value = asset_value
        self.monthly_income = monthly_income
        self.monthly_expenditure = monthly_expenditure
        self.debt = debt





