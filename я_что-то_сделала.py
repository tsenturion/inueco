p_speed = float(input())
v_speed = float(input())
if p_speed > v_speed:
    print('Петя')
else:
    print('Вася')

    p_speed = float(input())
v_speed = float(input())
t_speed = float(input())
if p_speed > v_speed and p_speed > t_speed:
    print("Петя")
elif v_speed > p_speed and v_speed > t_speed:
    print("Вася")
else:
    print("Толя")
    