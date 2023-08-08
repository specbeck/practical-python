# bounce.py
#
# Exercise 1.5

drop_height = 100
loss_fraction = 3 / 5

hit_num = 1

while hit_num <= 10:  
    drop_height *= loss_fraction # updates height every bounce
    print(hit_num, round(drop_height, 4))
    hit_num += 1 # increases hits