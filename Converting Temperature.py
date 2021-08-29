#python programme to convert temperature in celcius to fahrenheit
Cnum=float(input('enter the temperature in celcius:'))
Fnum=(Cnum*1.8)+32
print('%0.1f degree celsius is equal to %0.1f fahrenheit'%(Cnum,Fnum))
temp=Fnum
if(temp>=104):
    print('its hot')
elif(temp<=50):
    print('its cold')
else:
    print('the temperature is nice')