from decimal import*
import decimal
'''item=0.70
rate=1.05'''
item=Decimal(0.700)
rate=Decimal(1.050)
tax=item*rate
total=item+tax
#placeholder used using Format function
print('Hi I am {1:.2f} years old'.format(20,19))
#here in {1:.2f} 1==arguement index, .2=precision after decimal point, f==floating point number
#placeholder used without using Format function
print('Hi I am %.2f years old'%20)
print( 'Item:\t %.3f' %item )
print( 'Tax:\t %.3f' %tax )
print( 'Total:\t %.3f' % total )
print( 'Item:\t %.20f' %item )
print( 'Tax:\t %.20f' %tax )
print( 'Total:\t %.20f' % total )
