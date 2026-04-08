f_current = 3
f_prev=2
f_prevprev=1

total = 2

for i in range(1, 1000):
    f_next = f_current + f_prev
    f_prev = f_current
    f_current = f_next
    
    if f_next > 4000000:
        break
    
    if f_next % 2 == 0:
        total += f_next
            
print(total)
