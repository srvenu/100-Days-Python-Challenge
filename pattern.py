#pattern printing

row = 5
for i in range(0,row+1):
    print('*'*i)

print('\n')

for i in range(row,0,-1):
    print('*'*i)

print('\n')

for i in range(1,row+1):
    print(' '*(row-i)+'*'*(2*i-1))

print('\n')

for i in range(row,0,-1):
    print(' '*(row-i)+'*'*(i))

print('\n')

for i in range(row,0,-1):
    print(' '*(row-i)+'*'*(2*i-1))

print('\n')

for i in range(1,row+1):
    print(' '.join(str(j) for j in range(1,i+1)))

print('\n')

count=1
for i in range(1,row+1):
    for j in range(1,i+1):
        print(count,end=' ')
        count+=1
    print()