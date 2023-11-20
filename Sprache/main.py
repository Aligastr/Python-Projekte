#hi


list = []
with open("adjektive_a.txt", "r", encoding="utf-8") as f:
    for i in f:
        i = i.replace(" ","")
        #list.append(i.split(",")) funktioniert nicht richtig
        list = list + i.split(",")

count = 0
count_negativ = 0
print('Regeln: Für stop schreib "stop"')
for i in list:
    print(i)
    pruf = input('Geben Sie den Text ein: ')
    if pruf == 'stop' or pruf == 'Stop':
        print(f'Du hast  {count} Wörter richtig und  {count_negativ} Wörter falsch geschrieben.')
        break
    elif i == pruf:
        print('richtig')
        count += 1
    elif i != pruf:
        print('falsch')
        count_negativ += 1
    else:
        print('error')
        break

