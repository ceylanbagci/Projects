import sys
import math

"""
1.Clasify units
2.Convert

"""
def convert(frm,to,amount):
    try:
        frmm = metric_system[frm]
    except :
        frmm = us_customary_units[frm]

    try:
        too = metric_system[to]
    except :
        too = us_customary_units[to]

    return "{} {} = {} {}".format(amount,frm,frmm / too * amount,to)


metric_system = {'kilometer':  1000,
                'hectometer':  100,
                'decameter':   10,
                'meter': 1,
                'decimeter':   0.1,
                'centimeter':  0.01,
                'milimeter':  0.001}
us_customary_units = {'point':  0.35*10**(-3),
                      'pica':   4.233*10**(-3),
                      'inch':   25.4*10**(-3),
                      'foot':   0.3048,
                      'yard':   0.9144,
                      'mile':   1609.344}
unit_list = []
for item in metric_system:
    unit_list.append(item)
for item in us_customary_units:
    unit_list.append(item)

print("Please select one of them :",unit_list)
frm = input("Select unit from convert").lower()
amount = float(input("How long {} to convert".format(frm)))
to = input("Select unit to convert").lower()


print(convert(frm,to,amount))
