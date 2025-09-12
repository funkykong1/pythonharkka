ans = 0
lop = 0
#tähän ylläoleva numero +1
for i in range(3+1):
    #if i == 0:
        #continue
    # Tähän vakio jaettuna tai kertaa jollain
    ans = ((-1)**i)/(i**2+1)
    print(f"iteraatio #{i} = {ans}")
    lop += ans
print(lop)