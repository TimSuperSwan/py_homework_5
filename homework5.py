# _____________________________38________________________________
#  Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# words = 'нек кек! вабв. пам тук'
# list_words = words.split()

# result = list(filter(lambda x:'абв' not in x ,list_words))

# print(result)

# ___________________________39(2)._________________________
# Создайте программу для игры в ""Крестики-нолики"". 
# Игра реализуется в терминале, игроки ходят поочередно, 
# необходимо вывести карту(как удобнее, можно например в виде списка, 
# внутри которого будут 3 списка по 3 элемента, каждый из которого обозначает соответсвующие клетки от 1 до 9), 
# сделать проверку не занята ли клетка, на которую мы хотим поставить крестик или нолик, 
# и проверку на победу( стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)

# pole = [['_','_','_'],['_','_','_'],['_','_','_']]



# def print_table (mlist):
#     for i in range(len(mlist)):
#         print('|'.join(str(x) for x in mlist[i]))
# print_table(pole)

# def vvod (table,znak):
#     chek = True
#     while chek:
#         hod = input()
#         hod = list(map(int,hod.split()))
#         if table[hod[0]][hod[1]] == "x" or table[hod[0]][hod[1]] == "o":
#             print('место занято, целься лучше')        
#         if table[hod[0]][hod[1]] != "x" and table[hod[0]][hod[1]] != "o":
#             table[hod[0]][hod[1]] = znak
#             chek = False
        
#     print_table(table)

# def win_check (table):
#     win = table[0] + table [1] + table [2]
#     win_form = ((0,1,2),(3,4,5),(6,7,8),
#                (0,3,6),(1,4,7),(2,5,8),
#                (0,4,8),(2,4,6))
#     for i in win_form:
#         if win[i[0]] == win[i[1]] == win[i[2]] and win[i[0]] != '_' and win[i[1]] != '_' and win[i[2]] != '_':
#             return True
#     return False

# for i in range(9):
#     if i%2 == 1:
#         print('Ходят крестики:')
#         vvod(pole,'x')
#         if win_check(pole):
#             print('Ура! победили крестики')
#             break
#     else:
#         print('Ходят нолики:')
#         vvod(pole,'o')
#         if win_check(pole):
#             print('Ура! Победили нолики')
#             break

#_________________________40_________________________________
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.
    
strin = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'

def rle_sgatie (fresh):
    fresh = fresh + '0'
    char = fresh[0]
    count = 0
    result = ''
    for i in range(len(fresh)):
        if fresh[i] == char:
            count += 1
        # elif count == 1:
        #     result = result + "1" + char
        else:
            result = result + str(count) + char
            char = fresh[i]
            count = 1
    print(result)
            
def rle_raspakovka(stroka):
    result = ''
    number = ''
    for i in range(len(stroka)):
        if stroka[i].isdigit():
            number = number + stroka[i]
        else:
            result = result + stroka[i]*int(number)
            number = ''
    print(result)

rle_sgatie(strin)

rle_raspakovka('6A1F2D7C1A17E')







    