#ifndef LED_H
#define LED_H

#include <stdio.h>
#include <stdarg.h>

typedef struct {
	    int lower;
	        int upper;
} Position;

typedef struct {
	int R;
	float p;
	float I;
} option;

void _printf(const char *format, ...);
float _scanf();
void calc(float Vcc, float Vdd, float Idd, option *op1, option *op2);
Position binarySearch(float arr[], int low, int high, float target);
void rated_power(float resistance, float Vcc, float Vdd, float *Std_power, option *op);
void Sci_notation(float number, float * mantissa, int * exp);
float _pow(float mantissa, int exponent);

#endif
