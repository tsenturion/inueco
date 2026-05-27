chr = int(input())
hun = chr // 100
des = chr // 10 % 10
nea = chr % 10
diz = nea + des 
mac = des + hun 
if mac > diz:
    print(f'{mac}{diz}')
else:
    print(f'{diz}{mac}')
