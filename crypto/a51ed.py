import random

x = []
y = []
z = []
result = []
maj = 0
chbX = False
chbY = False
chbZ = False
chbCalc = []

#64비트 난수 생성
for i in range(19):
    x.append(random.randrange(0,2))

for i in range(22):
    y.append(random.randrange(0,2))
    
for i in range(23):
    z.append(random.randrange(0,2))

for i in range(64):
    maj = lambda q, w, e: 1 if q+w+e >= 2 else 0
    maj = maj(x[8], y[10], z[10])
    
    chb = lambda x, y, arr: chbCalc.append(arr[len(arr) - 1]) if x == y else False
    chbX, chbY, chbZ = chb(x[8], maj, x), chb(y[10], maj, y), chb(z[10], maj, z)
    
    out = 0
    
    if(chbCalc == 3):
        out = chbCalc[0] ^ chbCalc[1] ^ chbCalc[2]
    else:
        out = chbCalc[0] ^ chbCalc[1]
        
    result.append(out)

    a = (((x[18] ^ x[17]) ^ x[16]) ^ x[13])
    b = (y[21] ^y[20])
    c = (((z[22] ^ z[21]) ^ z[20]) ^ z[7])

    x.pop()
    y.pop()
    z.pop()

    x.insert(0, a)
    y.insert(0, b)
    z.insert(0, c)
    
    chbCalc.clear()

    
print(result)
