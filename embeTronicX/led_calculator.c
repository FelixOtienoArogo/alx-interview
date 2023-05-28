#include <stdio.h>
#include <stdarg.h>
#include "led.h"

float Std_resistor[] = {1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1};
float Std_power[] = {0.25, 0.5, 1.0, 2.0, 4.0};

/**                                                                             
 *binarySearch - a function that perform binary search               
 *                                                                              
 *@arr: the array
 *@low: low
 *@high: high
 *@target: target 
 *
 *Return: the position we are looking for
 */
Position binarySearch(float arr[], int low, int high, float target)
{
	    Position result;

	    while (low <= high)
	    {
		    int mid = low + (high - low) / 2;
		    if (arr[mid] == target)
		    {
			    result.lower = mid - 1;
			    result.upper = mid + 1;
			    return result;
		    }
		    else if (arr[mid] < target)
			    low = mid + 1;
		    else
			    high = mid - 1;
	    }
	    result.lower = high;
	    result.upper = low;
	    return result;
}
/**                                                                             
 *rated power - a function that gives the rated power and current               
 *                                                                              
 *@format: the format of the thing to be printed                                
 *                                                                              
 *Return: the given thing                                                       
 */
void rated_power(float resistance, float Vcc, float Vdd, float *Std_power, option *op)
{
	float current, power;
	current = (Vcc - Vdd) / resistance;
	op->I = current;
	power = current * current * resistance;
	Position pow = binarySearch(Std_power, 0, 4, power);
	op->p = Std_power[pow.upper];
	if (op->p == 0)
	{
	op->p = power;
	}
}
/**
 *sci_notation - a function that gives resistor value in sci notation
 *
 *@format: the format of the thing to be printed
 *
 *Return: the given thing
 */
void Sci_notation(float number, float * mantissa, int * exponent)
{
	*mantissa = number;
	*exponent = 0;

	if (*mantissa != 0)
	{
		while (*mantissa >= 10.0)
		{
		*mantissa /= 10.0;
		(*exponent)++;
		}
		while (*mantissa < 1.0)
		{
		*mantissa *= 10.0;
		(*exponent)--;
		}
	}
}
/**
 *sci_notation - a function that gives resistor value in sci notation
 *
 *@format: the format of the thing to be printed
 *
 *Return: the given thing
 */
float _pow(float mantissa, int exponent)
{
float result = mantissa;
if (exponent > 0)
	{
	while (exponent > 0)
		{
			result *= 10.0;
			exponent--;
		}
	}
else if (exponent < 0)
	{
	while (exponent < 0)
		{
		result /= 10.0;
		exponent++;
		}
	}
return result;
}
/**                                                                             
 *_printf - a function that produces output according to a format               
 *                                                                              
 *@format: the format of the thing to be printed                                
 *                                                                              
 *Return: the given thing                                                       
 */
void _printf(const char* format, ...)
{
    va_list args;
    va_start(args, format);

    while (*format != '\0')
    {
        if (*format == '%')
        {
            format++;

            switch (*format)
            {
		case 'f':
                {
                    double value = va_arg(args, double);
                    int intValue = (int)value;
                    double decimalPart = value - intValue;

                    // Print the integer part
                    printf("%d", intValue);

                    // Print the decimal part
                    if (decimalPart > 0)
                    {
                        putchar('.');
                        int decimalDigits = 6; // Number of decimal digits to print
                        while (decimalDigits > 0 && decimalPart > 0)
                        {
                            decimalPart *= 10;
                            int digit = (int)decimalPart;
                            putchar('0' + digit);
                            decimalPart -= digit;
                            decimalDigits--;
                        }
                    }
                    break;
                }
                case 'd':
                {
                    int num = va_arg(args, int);
                    int divisor = 1;

                    if (num < 0)
                    {
                        putchar('-');
                        num *= -1;
                    }

                    // Calculate the divisor for extracting digits
                    int temp = num;
                    while (temp > 9)
                    {
                        temp /= 10;
                        divisor *= 10;
                    }

                    // Extract and print each digit
                    while (divisor >= 1)
                    {
                        int digit = num / divisor;
                        putchar('0' + digit);
                        num %= divisor;
                        divisor /= 10;
                    }

                    break;
                }
                case 'c':
                {
                    int ch = va_arg(args, int);
                    putchar(ch);
                    break;
                }
                case 's':
                {
                    char* str = va_arg(args, char*);
                    while (*str != '\0')
                    {
                        putchar(*str);
                        str++;
                    }
                    break;
                }
                default:
                    putchar(*format);
                    break;
            }
        }
        else
        {
            putchar(*format);
        }

        format++;
    }

    va_end(args);
}

/**                                                                             
 *_printf - a function that produces output according to a format               
 *                                                                              
 *@format: the format of the thing to be printed                                
 *                                                                              
 *Return: the given thing                                                       
 */
float _scanf()
{
    int ch;
    int sign = 1;
    float value = 0.0;
    float decimal = 0.1;

    // Skip whitespace
    while ((ch = getchar()) == ' ' || ch == '\t' || ch == '\n');

    // Check for a sign
    if (ch == '-')
    {
        sign = -1;
        ch = getchar();
    }
    else if (ch == '+')
    {
        ch = getchar();
    }

    // Process integer part
    while (ch >= '0' && ch <= '9')
    {
        value = value * 10 + (ch - '0');
        ch = getchar();
    }

    // Process decimal part
    if (ch == '.')
    {
        ch = getchar();
        while (ch >= '0' && ch <= '9')
        {
            value += (ch - '0') * decimal;
            decimal /= 10;
            ch = getchar();
        }
    }

    // Discard non-digit characters
    while (ch != ' ' && ch != '\t' && ch != '\n' && ch != EOF)
    {
        ch = getchar();
    }

    return value * sign;
}

/**
 * calc - Calculates the value of the resistor
 *
 * Return: Nothing
 */
void calc(float Vcc, float Vdd, float Idd, option *op1, option *op2)
{
	float R1, rated = 0, current, mantissa;
	int exponent;
	R1 = (Vcc - Vdd) / Idd;
	Sci_notation(R1, &mantissa, &exponent);
	Position pos = binarySearch(Std_resistor, 0, 23, mantissa);
	op1->R = (int)(_pow(Std_resistor[pos.lower], exponent));
	op2->R = (int)(_pow(Std_resistor[pos.upper], exponent));
	rated_power(_pow(Std_resistor[pos.lower], exponent),Vcc,Vdd, Std_power, op1);
	rated_power(_pow(Std_resistor[pos.upper], exponent),Vcc,Vdd, Std_power, op2);
}
