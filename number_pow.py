#Простий скрипт для вирахування степенів
number = int(input('Основне число: '))
num_pow = int(input('Степінь: '))
power = 1
for power in range(num_pow):
    print('Число',number, 'в степені', power,'буде дорівнювати:',number**power)