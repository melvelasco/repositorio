## Creación de un objeto range
r = range(1,89)
## Mutabilidad: intentar modificar un elemento del range
### error
r[0]= 9

## Suma de ranges
### error
r_sum = r +range (20,50)
## Multiplicación por un entero
### error
r_mult = r * 6

## Slicing
### Sí se puede
r_slice = r[7:8]
print(r_slice)

## Conversión a lista y a tupla
r_list = list(r)
r_tuple = tuple(r_list)
print('tupla:',r_tuple)
print('lista:',r_list)






