#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include "led.h"

/**
 * main - Entry point
 *
 * Return: Always 0 (Success)
 */
int main(void)
{
	option op1, op2;
	op1.R = 0;
	op1.p = 0;
	op1.I = 0;
	op2.R = 0;
	op2.p = 0;
	op2.I = 0;
	float input_voltage, led_voltage, led_current, resistor;
	_printf("Input Voltage (VCC) in volt: ");
	input_voltage = _scanf();
	_printf("LED1 Voltage Drop in volt: ");
	led_voltage = _scanf();
	_printf("LED1 Target Current in ampere: ");
	led_current = _scanf();

	calc(input_voltage, led_voltage, led_current, &op1, &op2);

	_printf("\n");
	_printf("Option1:\n");
	_printf("R = %d ohm, %f watt\n", op1.R, op1.p);
	_printf("Resulting Current = %f ampere\n", op1.I);
	if (op1.p > 4)
	{
	_printf("The power rating required exceeds the maximum available\n");
	}
	_printf("\n");

	_printf("Option2:\n");
        _printf("R = %d ohm, %f watt\n", op2.R, op2.p);
        _printf("Resulting Current = %f ampere\n", op2.I);
	if (op2.p > 4)
        {
        _printf("The power rating required exceeds the maximum available\n");
        }

	return (0);
}
