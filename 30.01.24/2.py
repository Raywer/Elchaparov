a=10
b=5
c=0.5
for i in range(11):
    for j in range(21):
        for k in range(201):
          kg = i*a+a*j+k*c
          kr=i+j+k
          if (kr<=100) and kg == 100:
              print(f'Быков-{i}, коров-{j}, телят-{k}')