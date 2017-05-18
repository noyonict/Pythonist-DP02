print(''' Me is my mom's most lovely son.She calls me by "Baba" ''')
#
print("This is 'Python2'\\'python3' practice")
#


name = 'python3'
name2 = 'python2'
a = 10
b = 5
print(name+name2)
print(name,name2)
#print(name*name2)
print(name, a)

a = 12
b = '15'
c = 12.5
print(type(b))
print(int(c))

a = 7
b = 39
sum = a + b
mul = a*b
div = b/a
print(a, '+ ' , b, ' =', sum)
print(a, '* ' , b, ' =', mul)
print('{} + {} = {}' .format(a,b,sum))
print('%d + %d = %d' %(a,b, a+b))
print(b , '/', a, '=' , div)
print('%d /  %d = %.3f' % (b, a, div))
print('{} / {} = {:.03}'.format(b,a,div))
