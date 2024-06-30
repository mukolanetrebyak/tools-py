hour = int(input("Час початку події (години): "))
mins = int(input("Час початку події (хвилини): "))
dura = int(input("Тривалість події (хвилин): "))

#Визнчення годин і хвилин
h_dura = dura//60
m_dura = dura%60

w_hour = hour + h_dura
w_mins = mins + m_dura

print("Подія закінчиться о", w_hour,w_mins)

