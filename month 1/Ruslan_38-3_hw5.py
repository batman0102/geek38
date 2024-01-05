data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")

designations = []
codes = []

for item in data:
    if item in data:
        designations.append(item)
    elif item in data:
        codes.append(item)

operators = dict(zip(designations, codes))

non_functional_operators = ['Katel', 'Fonex']
for operator in non_functional_operators:
    operators.pop(operator, None)

operators['O!'] = ['0705', '0700', '0500']
operators['Megacom'] = ['0550', '0999', '0555']
operators['Beeline'] = ['0770', '0222', '0777']

for key, value in operators.items():
    print(key, ':', value)



