# def zegar(h, m):
#     u_h = h - 9
#     u_m = m - 0
#     kro_u = u_h, u_m
#     p_h = 7 - u_h
#     p_m = 60 - u_m
#     if p_m == 60:
#         p_m = 0
#         p_h += 1
#     kro_p = p_h, p_m
#     return kro_u, kro_p
#
# print(zegar(15, 0))

import datetime

def zegar(h = 'brak', m = 'brak'):
    if h == 'brak':
        a_c = datetime.datetime.now()
        h = a_c.hour
    if m == 'brak':
        a_c = datetime.datetime.now()
        m = a_c.minute
    u_h = h - 9
    u_m = m - 0
    kro_u = u_h, u_m
    p_h = 7 - u_h
    p_m = 60 - u_m
    if p_m == 60:
        p_m = 0
        p_h += 1
    kro_p = p_h, p_m
    return kro_u, kro_p

print(zegar(15, 0))
print(zegar())