'''Calcular a hipotenusa'''
'''
import math
catetoAd = float(input ("Digite o valor do cateto adjacente: "))

catetoOP = float(input ("Digite o valor do cateto oposto: "))

hipotenusa = catetoAd ** 2 + catetoOP ** 2
hipotenusa = math.sqrt (hipotenusa)

print ("A hipotenusa é", hipotenusa) '''

#também pode ser assim

catetoAd = float(input ("Digite o valor do cateto adjacente: "))
catetoOP = float(input ("Digite o valor do cateto oposto: "))

hipotenusa = (catetoAd ** 2 + catetoOP ** 2) **(1/2)
print ("A hipotenusa é {:.2f}" .format(hipotenusa)) 