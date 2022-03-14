n1 =float(input('digite seua primeira nota '))
n2= float(input('digite seua segunda nota para ver '))
m = (n1+n2)/2
print('sua nota media é  {:.1f}'.format(m))
if m >= 6:
    print ('sua média  foi boa ! Parabnes')
else:
    print('sua media foi ruim !  Bora Estudar !')

#ou podemos escrever assim  print('PARABENS' if m >= 6 else 'ESTUDE MAIS !')

