# Ejercicio 62: Tabla de Descuentos 
# Exercise 62: Discount Table
"""
Una tienda tiene 60% de descuento en una variedad de productos descontinuados.
El vendedor quisiera ayudar a sus clientes a determinar el costo a través de una tabla
que muestre el valor original y con el descuento 
Escriba un programa que use un ciclo para generar esta tabla,

A particular retailer is having a 60 percent off sale on a variety of discontinued
products. The retailer would like to help its customers determine the reduced price
of the merchandise by having a printed discount table on the shelf that shows the
original prices and the prices after the discount has been applied. Write a program that
uses a loop to generate this table, showing the original price, the discount amount,
and the new price for purchases of $4.95, $9.95, $14.95, $19.95 and $24.95. Ensure
that the discount amounts and the new prices are rounded to 2 decimal places when
they are displayed.
"""

prices = [4.95, 9.95, 14.95, 19.95, 24.95]

for i in prices:
    print(i,  i-i*0.6 )