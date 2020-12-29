print('Discount Calculator')
sCost = input('cost f the item: ')
sPercent = input('what percent discount is it ?: ')
fCost = float(sCost)
fPercent = float(sPercent)
fDiscount = fCost * fPercent / 100
print('you save : '+ str(fDiscount))
print('you pay : ' + str(fCost-fDiscount))
