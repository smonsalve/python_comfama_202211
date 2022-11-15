# Ejercicio 63: Tabla de conversión Temperatura
# Exercise 63: Temperature Conversion Table
# 
"""
Escriba un programa que muestre la tabla de conversión de temperatura para grados 
Centigrados y Farenheit. La tabla debe incluir filas para todas las temperaturas 
entre 0 y 100 °C que sean multiplos de 10. Incluya una fila de cabeceras.

Write a program that displays a temperature conversion table for degrees Celsius and
degrees Fahrenheit. The table should include rows for all temperatures between 0
and 100 degrees Celsius that are multiples of 10 degrees Celsius. Include appropriate
headings on your columns. The formula for converting between degrees Celsius and
degrees Fahrenheit can be found on the internet.
"""

for i in range(0,101,10):
    print(f"{i}°C -> {i*(9/5) + 32}°F")