#Гра з квіткою
'''
flower = "Спатифіллум"
flower_in = input("Введіть назву квітки: ")
if flower_in == flower:
    print("Так, Спатифіллум ‒ найкраща квітка на світі!")
    exit()
elif flower_in == "спатифіллум":
    print("Ні, я хочу спатифіллум великий!")
else:
    print("Спатифіллум! Не ",flower_in,"!")
'''
#Податковий калькулятор

'''
income = float(input("Введіть річний дохід: "))

if income < 85528:
    tax = income * 0.18 - 556.02
elif income > 85528:
    tax = 14839.02 + ((income-85528)*0.32)

if tax < 0:
    tax = 0.0 

tax = round(tax, 0)
print("Податок склав:", tax, "талера") 
'''
#Калькулятор високосного року

year = int(input("Введіть рік: "))

if year < 1582:
 print("Не в межах григоріанського календарного періоду")
else:
    if year % 4 !=0:
       print("Звичайний рік")
    elif year % 100 !=0:
       print("Високосний рік")
    elif year % 400 !=0:
       print("Звичайний рік")
    else:
       print("Високосний рік")


