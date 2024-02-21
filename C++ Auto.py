import tkinter as tk

from tkinter import ttk, scrolledtext



# Define the list of C++ program topics and their code

cpp_programs = {

    "Hello, World! Program": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tcout << "Hello, World!" << endl;\n\treturn 0;\n}',

    "Print Number Entered by User": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tint num;\n\tcout << "Enter a number: ";\n\tcin >> num;\n\tcout << "The number you entered is: " << num << endl;\n\treturn 0;\n}',

    "Add Two Numbers": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tint num1, num2, sum;\n\tcout << "Enter two numbers: ";\n\tcin >> num1 >> num2;\n\tsum = num1 + num2;\n\tcout << "Sum of " << num1 << " and " << num2 << " is: " << sum << endl;\n\treturn 0;\n}',

    "Find Quotient and Remainder": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tint dividend, divisor, quotient, remainder;\n\tcout << "Enter dividend: ";\n\tcin >> dividend;\n\tcout << "Enter divisor: ";\n\tcin >> divisor;\n\tquotient = dividend / divisor;\n\tremainder = dividend % divisor;\n\tcout << "Quotient = " << quotient << endl;\n\tcout << "Remainder = " << remainder << endl;\n\treturn 0;\n}',

    "Find Size of int, float, double and char": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tcout << "Size of int: " << sizeof(int) << " bytes" << endl;\n\tcout << "Size of float: " << sizeof(float) << " bytes" << endl;\n\tcout << "Size of double: " << sizeof(double) << " bytes" << endl;\n\tcout << "Size of char: " << sizeof(char) << " byte" << endl;\n\treturn 0;\n}',

    "Swap Two Numbers": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tint num1, num2, temp;\n\tcout << "Enter value of num1: ";\n\tcin >> num1;\n\tcout << "Enter value of num2: ";\n\tcin >> num2;\n\ttemp = num1;\n\tnum1 = num2;\n\tnum2 = temp;\n\tcout << "After swapping, num1 is: " << num1 << endl;\n\tcout << "After swapping, num2 is: " << num2 << endl;\n\treturn 0;\n}',

    "Check Whether Number is Even or Odd": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tint num;\n\tcout << "Enter an integer: ";\n\tcin >> num;\n\tif(num % 2 == 0)\n\t\tcout << num << " is even." << endl;\n\telse\n\t\tcout << num << " is odd." << endl;\n\treturn 0;\n}',

    "Check Whether a character is Vowel or Consonant": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tchar ch;\n\tcout << "Enter a character: ";\n\tcin >> ch;\n\tif (ch == \'a\' || ch == \'e\' || ch == \'i\' || ch == \'o\' || ch == \'u\' ||\n\t    ch == \'A\' || ch == \'E\' || ch == \'I\' || ch == \'O\' || ch == \'U\')\n\t\tcout << ch << " is a vowel." << endl;\n\telse\n\t\tcout << ch << " is a consonant." << endl;\n\treturn 0;\n}',

    "Find Largest Number Among Three Numbers": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tint num1, num2, num3;\n\tcout << "Enter three numbers: ";\n\tcin >> num1 >> num2 >> num3;\n\tif (num1 >= num2 && num1 >= num3)\n\t\tcout << "Largest number: " << num1 << endl;\n\telse if (num2 >= num1 && num2 >= num3)\n\t\tcout << "Largest number: " << num2 << endl;\n\telse\n\t\tcout << "Largest number: " << num3 << endl;\n\treturn 0;\n}',

    "Find All Roots of a Quadratic Equation": '#include <iostream>\n#include <cmath>\n\nusing namespace std;\n\nint main() {\n\tdouble a, b, c, discriminant, root1, root2, realPart, imaginaryPart;\n\tcout << "Enter coefficients a, b and c: ";\n\tcin >> a >> b >> c;\n\tdiscriminant = b * b - 4 * a * c;\n\tif (discriminant > 0) {\n\t\troot1 = (-b + sqrt(discriminant)) / (2 * a);\n\t\troot2 = (-b - sqrt(discriminant)) / (2 * a);\n\t\tcout << "Roots are real and different." << endl;\n\t\tcout << "Root1 = " << root1 << " and Root2 = " << root2 << endl;\n\t}\n\telse if (discriminant == 0) {\n\t\troot1 = root2 = -b / (2 * a);\n\t\tcout << "Roots are real and same." << endl;\n\t\tcout << "Root1 = Root2 = " << root1 << endl;\n\t}\n\telse {\n\t\trealPart = -b / (2 * a);\n\t\timaginaryPart = sqrt(-discriminant) / (2 * a);\n\t\tcout << "Roots are complex and different."  << endl;\n\t\tcout << "Root1 = " << realPart << " + " << imaginaryPart << "i and Root2 = " << realPart << " - " << imaginaryPart << "i" << endl;\n\t}\n\treturn 0;\n}',

    "Calculate Sum of Natural Numbers": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tint n, sum = 0;\n\tcout << "Enter a positive integer: ";\n\tcin >> n;\n\tfor (int i = 1; i <= n; ++i) {\n\t\tsum += i;\n\t}\n\tcout << "Sum = " << sum << endl;\n\treturn 0;\n}',

    "Check Leap Year": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tint year;\n\tbool isLeapYear = false;\n\tcout << "Enter a year: ";\n\tcin >> year;\n\tif (year % 4 == 0) {\n\t\tif (year % 100 == 0) {\n\t\t\tif (year % 400 == 0)\n\t\t\t\tisLeapYear = true;\n\t\t} else {\n\t\t\tisLeapYear = true;\n\t\t}\n\t}\n\tif (isLeapYear)\n\t\tcout << year << " is a leap year." << endl;\n\telse\n\t\tcout << year << " is not a leap year." << endl;\n\treturn 0;\n}',

    "Find Factorial": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tint n, factorial = 1;\n\tcout << "Enter a positive integer: ";\n\tcin >> n;\n\tfor (int i = 1; i <= n; ++i) {\n\t\tfactorial *= i;\n\t}\n\tcout << "Factorial of " << n << " = " << factorial << endl;\n\treturn 0;\n}',

    "Generate Multiplication Table": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tint n;\n\tcout << "Enter an integer: ";\n\tcin >> n;\n\tcout << "Multiplication Table of " << n << ":" << endl;\n\tfor (int i = 1; i <= 10; ++i) {\n\t\tcout << n << " * " << i << " = " << n * i << endl;\n\t}\n\treturn 0;\n}',

    "Display Fibonacci Series": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tint n, t1 = 0, t2 = 1, nextTerm;\n\tcout << "Enter the number of terms: ";\n\tcin >> n;\n\tcout << "Fibonacci Series: ";\n\tfor (int i = 1; i <= n; ++i) {\n\t\tcout << t1 << " + ";\n\t\tnextTerm = t1 + t2;\n\t\tt1 = t2;\n\t\tt2 = nextTerm;\n\t}\n\treturn 0;\n}',

    "Find GCD": '#include <iostream>\n\nusing namespace std;\n\nint gcd(int a, int b) {\n\tif (b == 0)\n\t\treturn a;\n\treturn gcd(b, a % b);\n}\n\nint main() {\n\tint num1, num2;\n\tcout << "Enter two numbers: ";\n\tcin >> num1 >> num2;\n\tcout << "GCD of " << num1 << " and " << num2 << " is: " << gcd(num1, num2) << endl;\n\treturn 0;\n}',

    "Find LCM": '#include <iostream>\n\nusing namespace std;\n\nint gcd(int a, int b) {\n\tif (b == 0)\n\t\treturn a;\n\treturn gcd(b, a % b);\n}\n\nint lcm(int a, int b) {\n\treturn (a * b) / gcd(a, b);\n}\n\nint main() {\n\tint num1, num2;\n\tcout << "Enter two numbers: ";\n\tcin >> num1 >> num2;\n\tcout << "LCM of " << num1 << " and " << num2 << " is: " << lcm(num1, num2) << endl;\n\treturn 0;\n}',

    "Reverse a Number": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tint n, reversedNumber = 0, remainder;\n\tcout << "Enter an integer: ";\n\tcin >> n;\n\twhile (n != 0) {\n\t\tremainder = n % 10;\n\t\treversedNumber = reversedNumber * 10 + remainder;\n\t\tn /= 10;\n\t}\n\tcout << "Reversed Number: " << reversedNumber << endl;\n\treturn 0;\n}',

    "Calculate Power of a Number": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tint base, exponent;\n\tlong long result = 1;\n\tcout << "Enter base and exponent: ";\n\tcin >> base >> exponent;\n\twhile (exponent != 0) {\n\t\tresult *= base;\n\t\t--exponent;\n\t}\n\tcout << "Result = " << result << endl;\n\treturn 0;\n}',

    "Increment ++ and Decrement -- Operator Overloading in C++ Programming": '#include <iostream>\n\nusing namespace std;\n\nclass Integer {\nprivate:\n\tint value;\npublic:\n\tInteger(int val) : value(val) {}\n\tvoid operator++() {\n\t\t++value;\n\t}\n\tvoid operator--() {\n\t\t--value;\n\t}\n\tvoid display() {\n\t\tcout << "Value: " << value << endl;\n\t}\n};\n\nint main() {\n\tInteger num(5);\n\tnum.display();\n\t++num;\n\tnum.display();\n\t--num;\n\tnum.display();\n\treturn 0;\n}',

    "Subtract Complex Number Using Operator Overloading": '#include <iostream>\n\nusing namespace std;\n\nclass Complex {\nprivate:\n\tdouble real;\n\tdouble imag;\npublic:\n\tComplex(double r, double i) : real(r), imag(i) {}\n\tComplex operator-(const Complex &obj) {\n\t\tdouble newReal = real - obj.real;\n\t\tdouble newImag = imag - obj.imag;\n\t\treturn Complex(newReal, newImag);\n\t}\n\tvoid display() {\n\t\tcout << "Result: " << real << " + " << imag << "i" << endl;\n\t}\n};\n\nint main() {\n\tComplex num1(4.5, 5.5);\n\tComplex num2(2.4, 3.5);\n\tComplex result = num1 - num2;\n\tresult.display();\n\treturn 0;\n}',

    "Find ASCII Value of a Character": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tchar c;\n\tcout << "Enter a character: ";\n\tcin >> c;\n\tcout << "ASCII Value of " << c << " is: " << int(c) << endl;\n\treturn 0;\n}',

    "Multiply two Numbers": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tfloat num1, num2, product;\n\tcout << "Enter two numbers: ";\n\tcin >> num1 >> num2;\n\tproduct = num1 * num2;\n\tcout << "Product = " << product << endl;\n\treturn 0;\n}',

    "Check Whether a Number is Palindrome or Not": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tint num, reversedNumber = 0, originalNumber, remainder;\n\tcout << "Enter an integer: ";\n\tcin >> num;\n\toriginalNumber = num;\n\twhile (num != 0) {\n\t\tremainder = num % 10;\n\t\treversedNumber = reversedNumber * 10 + remainder;\n\t\tnum /= 10;\n\t}\n\tif (originalNumber == reversedNumber)\n\t\tcout << originalNumber << " is a palindrome." << endl;\n\telse\n\t\tcout << originalNumber << " is not a palindrome." << endl;\n\treturn 0;\n}',

    "Check Whether a Number is Prime or Not": '#include <iostream>\n\nusing namespace std;\n\nbool isPrime(int n) {\n\tif (n <= 1)\n\t\treturn false;\n\tfor (int i = 2; i * i <= n; ++i) {\n\t\tif (n % i == 0)\n\t\t\treturn false;\n\t}\n\treturn true;\n}\n\nint main() {\n\tint num;\n\tcout << "Enter an integer: ";\n\tcin >> num;\n\tif (isPrime(num))\n\t\tcout << num << " is a prime number." << endl;\n\telse\n\t\tcout << num << " is not a prime number." << endl;\n\treturn 0;\n}',

    "Display Prime Numbers Between Two Intervals": '#include <iostream>\n\nusing namespace std;\n\nbool isPrime(int n) {\n\tif (n <= 1)\n\t\treturn false;\n\tfor (int i = 2; i * i <= n; ++i) {\n\t\tif (n % i == 0)\n\t\t\treturn false;\n\t}\n\treturn true;\n}\n\nint main() {\n\tint low, high;\n\tcout << "Enter two numbers (intervals): ";\n\tcin >> low >> high;\n\tcout << "Prime numbers between " << low << " and " << high << " are:" << endl;\n\tfor (int i = low; i <= high; ++i) {\n\t\tif (isPrime(i))\n\t\t\tcout << i << " ";\n\t}\n\tcout << endl;\n\treturn 0;\n}',

    "Check Armstrong Number": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tint num, originalNumber, remainder, result = 0;\n\tcout << "Enter an integer: ";\n\tcin >> num;\n\toriginalNumber = num;\n\twhile (originalNumber != 0) {\n\t\tremainder = originalNumber % 10;\n\t\tresult += remainder * remainder * remainder;\n\t\toriginalNumber /= 10;\n\t}\n\tif (result == num)\n\t\tcout << num << " is an Armstrong number." << endl;\n\telse\n\t\tcout << num << " is not an Armstrong number." << endl;\n\treturn 0;\n}',

    "Display Armstrong Number Between Two Intervals": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tint low, high, originalNumber, remainder, result;\n\tcout << "Enter two numbers (intervals): ";\n\tcin >> low >> high;\n\tcout << "Armstrong numbers between " << low << " and " << high << " are:" << endl;\n\tfor (int num = low + 1; num < high; ++num) {\n\t\toriginalNumber = num;\n\t\tresult = 0;\n\t\twhile (originalNumber != 0) {\n\t\t\tremainder = originalNumber % 10;\n\t\t\tresult += remainder * remainder * remainder;\n\t\t\toriginalNumber /= 10;\n\t\t}\n\t\tif (result == num)\n\t\t\tcout << num << " ";\n\t}\n\tcout << endl;\n\treturn 0;\n}',

    "Display Factors of a Number": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tint num;\n\tcout << "Enter a positive integer: ";\n\tcin >> num;\n\tcout << "Factors of " << num << " are:" << endl;\n\tfor (int i = 1; i <= num; ++i) {\n\t\tif (num % i == 0)\n\t\t\tcout << i << " ";\n\t}\n\tcout << endl;\n\treturn 0;\n}',

    "Create Pyramid and Pattern": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tint rows;\n\tcout << "Enter number of rows: ";\n\tcin >> rows;\n\tfor (int i = 1; i <= rows; ++i) {\n\t\tfor (int j = 1; j <= i; ++j) {\n\t\t\tcout << "* ";\n\t\t}\n\t\tcout << endl;\n\t}\n\treturn 0;\n}',

    "Sum of Natural Numbers using Recursion": '#include <iostream>\n\nusing namespace std;\n\nint sum(int n) {\n\tif (n != 0)\n\t\treturn n + sum(n - 1);\n\telse\n\t\treturn n;\n}\n\nint main() {\n\tint n;\n\tcout << "Enter a positive integer: ";\n\tcin >> n;\n\tcout << "Sum = " << sum(n) << endl;\n\treturn 0;\n}',

    "Calculate Factorial of a Number Using Recursion": '#include <iostream>\n\nusing namespace std;\n\nunsigned long long factorial(int n) {\n\tif (n == 0)\n\t\treturn 1;\n\treturn n * factorial(n - 1);\n}\n\nint main() {\n\tint n;\n\tcout << "Enter a positive integer: ";\n\tcin >> n;\n\tcout << "Factorial of " << n << " = " << factorial(n) << endl;\n\treturn 0;\n}',

    "Find G.C.D Using Recursion": '#include <iostream>\n\nusing namespace std;\n\nint gcd(int a, int b) {\n\tif (b == 0)\n\t\treturn a;\n\treturn gcd(b, a % b);\n}\n\nint main() {\n\tint num1, num2;\n\tcout << "Enter two positive integers: ";\n\tcin >> num1 >> num2;\n\tcout << "GCD of " << num1 << " and " << num2 << " is: " << gcd(num1, num2) << endl;\n\treturn 0;\n}',

    "Convert Binary Number to Decimal and vice-versa": '#include <iostream>\n#include <cmath>\n\nusing namespace std;\n\nint binaryToDecimal(long long n) {\n\tint decimalNumber = 0, i = 0, remainder;\n\twhile (n != 0) {\n\t\tremainder = n % 10;\n\t\tn /= 10;\n\t\tdecimalNumber += remainder * pow(2, i);\n\t\t++i;\n\t}\n\treturn decimalNumber;\n}\n\nlong long decimalToBinary(int n) {\n\tlong long binaryNumber = 0;\n\tint remainder, i = 1, step = 1;\n\twhile (n != 0) {\n\t\tremainder = n % 2;\n\t\tn /= 2;\n\t\tbinaryNumber += remainder * i;\n\t\ti *= 10;\n\t}\n\treturn binaryNumber;\n}\n\nint main() {\n\tint choice, decimal;\n\tlong long binary;\n\tcout << "Enter your choice (1 for binary to decimal, 2 for decimal to binary): ";\n\tcin >> choice;\n\tif (choice == 1) {\n\t\tcout << "Enter a binary number: ";\n\t\tcin >> binary;\n\t\tcout << "Decimal equivalent: " << binaryToDecimal(binary) << endl;\n\t} else if (choice == 2) {\n\t\tcout << "Enter a decimal number: ";\n\t\tcin >> decimal;\n\t\tcout << "Binary equivalent: " << decimalToBinary(decimal) << endl;\n\t} else {\n\t\tcout << "Invalid choice." << endl;\n\t}\n\treturn 0;\n}',

    "Convert Octal Number to Decimal and vice-versa": '#include <iostream>\n#include <cmath>\n\nusing namespace std;\n\nint octalToDecimal(int octalNumber) {\n\tint decimalNumber = 0, i = 0, remainder;\n\twhile (octalNumber != 0) {\n\t\tremainder = octalNumber % 10;\n\t\toctalNumber /= 10;\n\t\tdecimalNumber += remainder * pow(8, i);\n\t\t++i;\n\t}\n\treturn decimalNumber;\n}\n\nint decimalToOctal(int decimalNumber) {\n\tint octalNumber = 0, i = 1;\n\twhile (decimalNumber != 0) {\n\t\toctalNumber += (decimalNumber % 8) * i;\n\t\tdecimalNumber /= 8;\n\t\ti *= 10;\n\t}\n\treturn octalNumber;\n}\n\nint main() {\n\tint choice, decimal, octal;\n\tcout << "Enter your choice (1 for octal to decimal, 2 for decimal to octal): ";\n\tcin >> choice;\n\tif (choice == 1) {\n\t\tcout << "Enter an octal number: ";\n\t\tcin >> octal;\n\t\tcout << "Decimal equivalent: " << octalToDecimal(octal) << endl;\n\t} else if (choice == 2) {\n\t\tcout << "Enter a decimal number: ";\n\t\tcin >> decimal;\n\t\tcout << "Octal equivalent: " << decimalToOctal(decimal) << endl;\n\t} else {\n\t\tcout << "Invalid choice." << endl;\n\t}\n\treturn 0;\n}',

    "Convert Binary Number to Octal and vice-versa": '#include <iostream>\n\nusing namespace std;\n\nint binaryToDecimal(long long n) {\n\tint decimalNumber = 0, i = 0, remainder;\n\twhile (n != 0) {\n\t\tremainder = n % 10;\n\t\tn /= 10;\n\t\tdecimalNumber += remainder * pow(2, i);\n\t\t++i;\n\t}\n\treturn decimalNumber;\n}\n\nlong long decimalToBinary(int n) {\n\tlong long binaryNumber = 0;\n\tint remainder, i = 1, step = 1;\n\twhile (n != 0) {\n\t\tremainder = n % 2;\n\t\tn /= 2;\n\t\tbinaryNumber += remainder * i;\n\t\ti *= 10;\n\t}\n\treturn binaryNumber;\n}\n\nint decimalToOctal(int decimalNumber) {\n\tint octalNumber = 0, i = 1;\n\twhile (decimalNumber != 0) {\n\t\toctalNumber += (decimalNumber % 8) * i;\n\t\tdecimalNumber /= 8;\n\t\ti *= 10;\n\t}\n\treturn octalNumber;\n}\n\nlong long octalToBinary(int octalNumber) {\n\tlong long binaryNumber = 0;\n\tint decimalNumber = 0, i = 0;\n\twhile (octalNumber != 0) {\n\t\tdecimalNumber += (octalNumber % 10) * pow(8, i);\n\t\t++i;\n\t\toctalNumber /= 10;\n\t}\n\ti = 1;\n\twhile (decimalNumber != 0) {\n\t\tbinaryNumber += (decimalNumber % 2) * i;\n\t\tdecimalNumber /= 2;\n\t\ti *= 10;\n\t}\n\treturn binaryNumber;\n}\n\nint main() {\n\tint choice, octal, decimal;\n\tlong long binary;\n\tcout << "Enter your choice (1 for binary to octal, 2 for octal to binary): ";\n\tcin >> choice;\n\tif (choice == 1) {\n\t\tcout << "Enter a binary number: ";\n\t\tcin >> binary;\n\t\tdecimal = binaryToDecimal(binary);\n\t\tcout << "Octal equivalent: " << decimalToOctal(decimal) << endl;\n\t} else if (choice == 2) {\n\t\tcout << "Enter an octal number: ";\n\t\tcin >> octal;\n\t\tcout << "Binary equivalent: " << octalToBinary(octal) << endl;\n\t} else {\n\t\tcout << "Invalid choice." << endl;\n\t}\n\treturn 0;\n}',

    "Reverse a Sentence Using Recursion": '#include <iostream>\n#include <cstring>\n\nusing namespace std;\n\nvoid reverseSentence() {\n\tchar c;\n\tcin.get(c);\n\tif (c != \'\\n\') {\n\t\treverseSentence();\n\t\tcout << c;\n\t}\n}\n\nint main() {\n\tcout << "Enter a sentence: ";\n\treverseSentence();\n\treturn 0;\n}',

    "Calculate Average of Numbers Using Arrays": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tint n;\n\tcout << "Enter the number of data points: ";\n\tcin >> n;\n\tdouble arr[n], sum = 0.0, average;\n\tcout << "Enter " << n << " numbers: ";\n\tfor (int i = 0; i < n; ++i) {\n\t\tcin >> arr[i];\n\t\tsum += arr[i];\n\t}\n\taverage = sum / n;\n\tcout << "Average = " << average << endl;\n\treturn 0;\n}',

    "Find Largest Element of an Array": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tint n;\n\tcout << "Enter the number of elements in array: ";\n\tcin >> n;\n\tint arr[n];\n\tcout << "Enter elements of array: ";\n\tfor (int i = 0; i < n; ++i) {\n\t\tcin >> arr[i];\n\t}\n\tint largest = arr[0];\n\tfor (int i = 1; i < n; ++i) {\n\t\tif (arr[i] > largest)\n\t\t\tlargest = arr[i];\n\t}\n\tcout << "Largest element = " << largest << endl;\n\treturn 0;\n}',

    "Calculate Standard Deviation": '#include <iostream>\n#include <cmath>\n\nusing namespace std;\n\nint main() {\n\tint n;\n\tcout << "Enter the number of data points: ";\n\tcin >> n;\n\tdouble arr[n], sum = 0.0, mean, standardDeviation = 0.0;\n\tcout << "Enter " << n << " numbers: ";\n\tfor (int i = 0; i < n; ++i) {\n\t\tcin >> arr[i];\n\t\tsum += arr[i];\n\t}\n\tmean = sum / n;\n\tfor (int i = 0; i < n; ++i) {\n\t\tstandardDeviation += pow(arr[i] - mean, 2);\n\t}\n\tcout << "Standard Deviation = " << sqrt(standardDeviation / n) << endl;\n\treturn 0;\n}',

    "Add Two Matrix Using Multi-dimensional Arrays": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tint rows, cols;\n\tcout << "Enter number of rows and columns: ";\n\tcin >> rows >> cols;\n\tint matrix1[rows][cols], matrix2[rows][cols], sum[rows][cols];\n\tcout << "Enter elements of first matrix:" << endl;\n\tfor (int i = 0; i < rows; ++i) {\n\t\tfor (int j = 0; j < cols; ++j) {\n\t\t\tcin >> matrix1[i][j];\n\t\t}\n\t}\n\tcout << "Enter elements of second matrix:" << endl;\n\tfor (int i = 0; i < rows; ++i) {\n\t\tfor (int j = 0; j < cols; ++j) {\n\t\t\tcin >> matrix2[i][j];\n\t\t}\n\t}\n\tfor (int i = 0; i < rows; ++i) {\n\t\tfor (int j = 0; j < cols; ++j) {\n\t\t\tsum[i][j] = matrix1[i][j] + matrix2[i][j];\n\t\t}\n\t}\n\tcout << "Sum of matrices:" << endl;\n\tfor (int i = 0; i < rows; ++i) {\n\t\tfor (int j = 0; j < cols; ++j) {\n\t\t\tcout << sum[i][j] << " ";\n\t\t}\n\t\tcout << endl;\n\t}\n\treturn 0;\n}',

    "Multiply Two Matrix Using Multi-dimensional Arrays": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tint rows1, cols1, rows2, cols2;\n\tcout << "Enter rows and columns for first matrix: ";\n\tcin >> rows1 >> cols1;\n\tcout << "Enter rows and columns for second matrix: ";\n\tcin >> rows2 >> cols2;\n\tif (cols1 != rows2) {\n\t\tcout << "Error! Columns of first matrix not equal to rows of second." << endl;\n\t\treturn 0;\n\t}\n\tint matrix1[rows1][cols1], matrix2[rows2][cols2], product[rows1][cols2];\n\tcout << "Enter elements of first matrix:" << endl;\n\tfor (int i = 0; i < rows1; ++i) {\n\t\tfor (int j = 0; j < cols1; ++j) {\n\t\t\tcin >> matrix1[i][j];\n\t\t}\n\t}\n\tcout << "Enter elements of second matrix:" << endl;\n\tfor (int i = 0; i < rows2; ++i) {\n\t\tfor (int j = 0; j < cols2; ++j) {\n\t\t\tcin >> matrix2[i][j];\n\t\t}\n\t}\n\tfor (int i = 0; i < rows1; ++i) {\n\t\tfor (int j = 0; j < cols2; ++j) {\n\t\t\tproduct[i][j] = 0;\n\t\t\tfor (int k = 0; k < cols1; ++k) {\n\t\t\t\tproduct[i][j] += matrix1[i][k] * matrix2[k][j];\n\t\t\t}\n\t\t}\n\t}\n\tcout << "Product of matrices:" << endl;\n\tfor (int i = 0; i < rows1; ++i) {\n\t\tfor (int j = 0; j < cols2; ++j) {\n\t\t\tcout << product[i][j] << " ";\n\t\t}\n\t\tcout << endl;\n\t}\n\treturn 0;\n}',

    "Find Transpose of a Matrix": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tint rows, cols;\n\tcout << "Enter number of rows and columns: ";\n\tcin >> rows >> cols;\n\tint matrix[rows][cols], transpose[cols][rows];\n\tcout << "Enter elements of matrix:" << endl;\n\tfor (int i = 0; i < rows; ++i) {\n\t\tfor (int j = 0; j < cols; ++j) {\n\t\t\tcin >> matrix[i][j];\n\t\t}\n\t}\n\tfor (int i = 0; i < rows; ++i) {\n\t\tfor (int j = 0; j < cols; ++j) {\n\t\t\ttranspose[j][i] = matrix[i][j];\n\t\t}\n\t}\n\tcout << "Transpose of the matrix:" << endl;\n\tfor (int i = 0; i < cols; ++i) {\n\t\tfor (int j = 0; j < rows; ++j) {\n\t\t\tcout << transpose[i][j] << " ";\n\t\t}\n\t\tcout << endl;\n\t}\n\treturn 0;\n}',

    "Multiply two Matrices by Passing Matrix to Function": '#include <iostream>\n\nusing namespace std;\n\nvoid multiplyMatrix(int firstMatrix[][10], int secondMatrix[][10], int result[][10], int rowsFirst, int colsFirst, int rowsSecond, int colsSecond) {\n\tfor (int i = 0; i < rowsFirst; ++i) {\n\t\tfor (int j = 0; j < colsSecond; ++j) {\n\t\t\tresult[i][j] = 0;\n\t\t}\n\t}\n\tfor (int i = 0; i < rowsFirst; ++i) {\n\t\tfor (int j = 0; j < colsSecond; ++j) {\n\t\t\tfor (int k = 0; k < colsFirst; ++k) {\n\t\t\t\tresult[i][j] += firstMatrix[i][k] * secondMatrix[k][j];\n\t\t\t}\n\t\t}\n\t}\n}\n\nint main() {\n\tint rowsFirst, colsFirst, rowsSecond, colsSecond;\n\tint firstMatrix[10][10], secondMatrix[10][10], result[10][10];\n\tcout << "Enter rows and columns for first matrix: ";\n\tcin >> rowsFirst >> colsFirst;\n\tcout << "Enter rows and columns for second matrix: ";\n\tcin >> rowsSecond >> colsSecond;\n\tif (colsFirst != rowsSecond) {\n\t\tcout << "Error! Columns of first matrix not equal to rows of second." << endl;\n\t\treturn 0;\n\t}\n\tcout << "Enter elements of first matrix:" << endl;\n\tfor (int i = 0; i < rowsFirst; ++i) {\n\t\tfor (int j = 0; j < colsFirst; ++j) {\n\t\t\tcin >> firstMatrix[i][j];\n\t\t}\n\t}\n\tcout << "Enter elements of second matrix:" << endl;\n\tfor (int i = 0; i < rowsSecond; ++i) {\n\t\tfor (int j = 0; j < colsSecond; ++j) {\n\t\t\tcin >> secondMatrix[i][j];\n\t\t}\n\t}\n\tmultiplyMatrix(firstMatrix, secondMatrix, result, rowsFirst, colsFirst, rowsSecond, colsSecond);\n\tcout << "Product of matrices:" << endl;\n\tfor (int i = 0; i < rowsFirst; ++i) {\n\t\tfor (int j = 0; j < colsSecond; ++j) {\n\t\t\tcout << result[i][j] << " ";\n\t\t}\n\t\tcout << endl;\n\t}\n\treturn 0;\n}',

    "Access Elements of an Array Using Pointer": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tint data[5];\n\tcout << "Enter elements: ";\n\tfor (int i = 0; i < 5; ++i)\n\t\tcin >> data[i];\n\tcout << "You entered: ";\n\tfor (int i = 0; i < 5; ++i)\n\t\tcout << *(data + i) << " ";\n\treturn 0;\n}',

    "Swap Numbers in Cyclic Order Using Call by Reference": '#include <iostream>\n\nusing namespace std;\n\nvoid cyclicSwap(int *a, int *b, int *c) {\n\tint temp = *b;\n\t*b = *a;\n\t*a = *c;\n\t*c = temp;\n}\n\nint main() {\n\tint a, b, c;\n\tcout << "Enter a, b and c respectively: ";\n\tcin >> a >> b >> c;\n\tcout << "Before swapping: a = " << a << ", b = " << b << ", c = " << c << endl;\n\tcyclicSwap(&a, &b, &c);\n\tcout << "After swapping: a = " << a << ", b = " << b << ", c = " << c << endl;\n\treturn 0;\n}',

    "Find the Frequency of Characters in a String": '#include <iostream>\n#include <cstring>\n\nusing namespace std;\n\nint main() {\n\tchar str[100];\n\tint freq[256] = {0};\n\tcout << "Enter a string: ";\n\tcin.getline(str, 100);\n\tfor (int i = 0; str[i] != \'\\0\'; ++i) {\n\t\t++freq[str[i]];\n\t}\n\tcout << "Frequency of characters in the string: " << endl;\n\tfor (int i = 0; i < 256; ++i) {\n\t\tif (freq[i] != 0) {\n\t\t\tcout << (char)i << " appears " << freq[i] << " times" << endl;\n\t\t}\n\t}\n\treturn 0;\n}',

    "Find the Number of Vowels, Consonants, Digits and White Spaces in a String": '#include <iostream>\n#include <cctype>\n\nusing namespace std;\n\nint main() {\n\tchar line[150];\n\tint vowels, consonants, digits, spaces;\n\tvowels = consonants = digits = spaces = 0;\n\tcout << "Enter a line of string: ";\n\tcin.getline(line, 150);\n\tfor (int i = 0; line[i] != \'\\0\'; ++i) {\n\t\tif (isalpha(line[i])) {\n\t\t\tswitch (tolower(line[i])) {\n\t\t\tcase \'a\':\n\t\t\tcase \'e\':\n\t\t\tcase \'i\':\n\t\t\tcase \'o\':\n\t\t\tcase \'u\':\n\t\t\t\t++vowels;\n\t\t\t\tbreak;\n\t\t\tdefault:\n\t\t\t\t++consonants;\n\t\t\t}\n\t\t} else if (isdigit(line[i])) {\n\t\t\t++digits;\n\t\t} else if (line[i] == \' \') {\n\t\t\t++spaces;\n\t\t}\n\t}\n\tcout << "Vowels: " << vowels << endl;\n\tcout << "Consonants: " << consonants << endl;\n\tcout << "Digits: " << digits << endl;\n\tcout << "White spaces: " << spaces << endl;\n\treturn 0;\n}',

    "Remove all Characters in a String Except Alphabets.": '#include <iostream>\n#include <cctype>\n#include <cstring>\n\nusing namespace std;\n\nint main() {\n\tchar line[150];\n\tcout << "Enter a string: ";\n\tcin.getline(line, 150);\n\tfor (int i = 0; line[i] != \'\\0\'; ++i) {\n\t\tif ((line[i] >= \'a\' && line[i] <= \'z\') || (line[i] >= \'A\' && line[i] <= \'Z\'))\n\t\t\tcout << line[i];\n\t}\n\treturn 0;\n}',

    "Find the Length of a String": '#include <iostream>\n#include <cstring>\n\nusing namespace std;\n\nint main() {\n\tchar str[100];\n\tint length;\n\tcout << "Enter a string: ";\n\tcin.getline(str, 100);\n\tlength = strlen(str);\n\tcout << "Length of \\"" << str << "\\" is " << length << endl;\n\treturn 0;\n}',

    "Concatenate Two Strings": '#include <iostream>\n#include <cstring>\n\nusing namespace std;\n\nint main() {\n\tchar str1[100], str2[100];\n\tcout << "Enter first string: ";\n\tcin.getline(str1, 100);\n\tcout << "Enter second string: ";\n\tcin.getline(str2, 100);\n\tstrcat(str1, str2);\n\tcout << "Concatenated string: " << str1 << endl;\n\treturn 0;\n}',

    "Copy Strings": '#include <iostream>\n#include <cstring>\n\nusing namespace std;\n\nint main() {\n\tchar source[100], destination[100];\n\tcout << "Enter source string: ";\n\tcin.getline(source, 100);\n\tstrcpy(destination, source);\n\tcout << "Destination string after copying: " << destination << endl;\n\treturn 0;\n}',

    "Sort Elements in Lexicographical Order (Dictionary Order)": '#include <iostream>\n#include <cstring>\n\nusing namespace std;\n\nint main() {\n\tchar str[5][50], temp[50];\n\tcout << "Enter 5 strings: " << endl;\n\tfor (int i = 0; i < 5; ++i)\n\t\tcin >> str[i];\n\tfor (int i = 0; i < 5; ++i) {\n\t\tfor (int j = i + 1; j < 5; ++j) {\n\t\t\tif (strcmp(str[i], str[j]) > 0) {\n\t\t\t\tstrcpy(temp, str[i]);\n\t\t\t\tstrcpy(str[i], str[j]);\n\t\t\t\tstrcpy(str[j], temp);\n\t\t\t}\n\t\t}\n\t}\n\tcout << "In lexicographical order: " << endl;\n\tfor (int i = 0; i < 5; ++i)\n\t\tcout << str[i] << endl;\n\treturn 0;\n}',

    "Store Information of a Student in a Structure": '#include <iostream>\n#include <cstring>\n\nusing namespace std;\n\nstruct Student {\n\tchar name[50];\n\tint roll;\n\tfloat marks;\n};\n\nint main() {\n\tStudent s;\n\tcout << "Enter information," << endl;\n\tcout << "Enter name: ";\n\tcin >> s.name;\n\tcout << "Enter roll number: ";\n\tcin >> s.roll;\n\tcout << "Enter marks: ";\n\tcin >> s.marks;\n\tcout << "\nDisplaying Information," << endl;\n\tcout << "Name: " << s.name << endl;\n\tcout << "Roll: " << s.roll << endl;\n\tcout << "Marks: " << s.marks << endl;\n\treturn 0;\n}',

    "Add Two Distances (in inch-feet) System Using Structures": '#include <iostream>\n\nusing namespace std;\n\nstruct Distance {\n\tint feet;\n\tfloat inch;\n} d1, d2, sum;\n\nint main() {\n\tcout << "Enter first distance," << endl;\n\tcout << "Enter feet: ";\n\tcin >> d1.feet;\n\tcout << "Enter inch: ";\n\tcin >> d1.inch;\n\tcout << "Enter second distance," << endl;\n\tcout << "Enter feet: ";\n\tcin >> d2.feet;\n\tcout << "Enter inch: ";\n\tcin >> d2.inch;\n\tsum.feet = d1.feet + d2.feet;\n\tsum.inch = d1.inch + d2.inch;\n\twhile (sum.inch >= 12.0) {\n\t\tsum.inch -= 12.0;\n\t\t++sum.feet;\n\t}\n\tcout << "Sum of distances = " << sum.feet << "\'-" << sum.inch << "\"" << endl;\n\treturn 0;\n}',

    "Add Complex Numbers by Passing Structure to a Function": '#include <iostream>\n\nusing namespace std;\n\nstruct Complex {\n\tfloat real;\n\tfloat imag;\n};\n\nComplex add(Complex n1, Complex n2) {\n\tComplex temp;\n\ttemp.real = n1.real + n2.real;\n\ttemp.imag = n1.imag + n2.imag;\n\treturn temp;\n}\n\nint main() {\n\tComplex num1, num2, temp;\n\tcout << "For first complex number," << endl;\n\tcout << "Enter real and imaginary parts respectively:" << endl;\n\tcin >> num1.real >> num1.imag;\n\tcout << "For second complex number," << endl;\n\tcout << "Enter real and imaginary parts respectively:" << endl;\n\tcin >> num2.real >> num2.imag;\n\ttemp = add(num1, num2);\n\tcout << "Sum = " << temp.real << " + " << temp.imag << "i";\n\treturn 0;\n}',

    "Calculate Difference Between Two Time Period": '#include <iostream>\n\nusing namespace std;\n\nstruct Time {\n\tint hours;\n\tint minutes;\n\tint seconds;\n};\n\nint main() {\n\tTime t1, t2, difference;\n\tcout << "Enter start time." << endl;\n\tcout << "Enter hours, minutes and seconds respectively: ";\n\tcin >> t1.hours >> t1.minutes >> t1.seconds;\n\tcout << "Enter end time." << endl;\n\tcout << "Enter hours, minutes and seconds respectively: ";\n\tcin >> t2.hours >> t2.minutes >> t2.seconds;\n\tdifference.seconds = t2.seconds - t1.seconds;\n\tdifference.minutes = t2.minutes - t1.minutes;\n\tdifference.hours = t2.hours - t1.hours;\n\tif (difference.seconds < 0) {\n\t\tdifference.seconds += 60;\n\t\t--difference.minutes;\n\t}\n\tif (difference.minutes < 0) {\n\t\tdifference.minutes += 60;\n\t\t--difference.hours;\n\t}\n\tcout << "Time difference = " << difference.hours << ":" << difference.minutes << ":" << difference.seconds;\n\treturn 0;\n}',

    "Store and Display Information Using Structure": '#include <iostream>\n#include <cstring>\n\nusing namespace std;\n\nstruct Person {\n\tchar name[50];\n\tint age;\n\tfloat salary;\n};\n\nint main() {\n\tPerson p;\n\tcout << "Enter Full name: ";\n\tcin.get(p.name, 50);\n\tcout << "Enter age: ";\n\tcin >> p.age;\n\tcout << "Enter salary: ";\n\tcin >> p.salary;\n\tcout << "\nDisplaying Information." << endl;\n\tcout << "Name: " << p.name << endl;\n\tcout << "Age: " << p.age << endl;\n\tcout << "Salary: " << p.salary << endl;\n\treturn 0;\n}'

    "Simple Interest Calculator" '#include <iostream>\n\nusing namespace std;\n\nint main() {\n    double principle, rate, time, SI;\n    \n    cout << "Enter principle amount: ";\n    cin >> principle;\n    \n    cout << "Enter rate of interest: ";\n    cin >> rate;\n    \n    cout << "Enter time (in years): ";\n    cin >> time;\n    \n    SI = (principle * rate * time) / 100;\n    \n    cout << "Simple Interest = " << SI;\n    \n    return 0;\n}\n'

     "Simple Interest Calculator" '''#include <iostream>

using namespace std;

int main() {
    double principle, rate, time, SI;
    
    cout << "Enter principle amount: ";
    cin >> principle;
    
    cout << "Enter rate of interest: ";
    cin >> rate;
    
    cout << "Enter time (in years): ";
    cin >> time;
    
    SI = (principle * rate * time) / 100;
    
    cout << "Simple Interest = " << SI;
    
    return 0;
}''',

    "Calculate Factorial": '''#include <iostream>

using namespace std;

int main() {
    int n, factorial = 1;
    cout << "Enter a positive integer: ";
    cin >> n;
    for (int i = 1; i <= n; ++i) {
        factorial *= i;
    }
    cout << "Factorial of " << n << " = " << factorial << endl;
    return 0;
}''',
"Check Prime Number": '''#include <iostream>

using namespace std;

int main() {
    int num, i;
    bool isPrime = true;
    
    cout << "Enter a positive integer: ";
    cin >> num;
    
    for (i = 2; i <= num / 2; ++i) {
        if (num % i == 0) {
            isPrime = false;
            break;
        }
    }
    
    if (isPrime)
        cout << num << " is a prime number.";
    else
        cout << num << " is not a prime number.";
    
    return 0;
}''',

"Linear Search": '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tint arr[] = {1, 2, 3, 4, 5};\n\tint target, n = sizeof(arr) / sizeof(arr[0]);\n\tcout << "Enter the element to search: ";\n\tcin >> target;\n\tbool found = false;\n\tfor (int i = 0; i < n; ++i) {\n\t\tif (arr[i] == target) {\n\t\t\tfound = true;\n\t\t\tbreak;\n\t\t}\n\t}\n\tif (found)\n\t\tcout << "Element found in the array." << endl;\n\telse\n\t\tcout << "Element not found in the array." << endl;\n\treturn 0;\n}',

"Binary Search": '#include <iostream>\n\nint binarySearch(int arr[], int left, int right, int target) {\n\twhile (left <= right) {\n\t\tint mid = left + (right - left) / 2;\n\t\tif (arr[mid] == target)\n\t\t\treturn mid;\n\t\tif (arr[mid] < target)\n\t\t\tleft = mid + 1;\n\t\telse\n\t\t\tright = mid - 1;\n\t}\n\treturn -1;\n}\n\nint main() {\n\tint arr[] = {1, 2, 3, 4, 5};\n\tint n = sizeof(arr) / sizeof(arr[0]);\n\tint target = 4;\n\tint result = binarySearch(arr, 0, n - 1, target);\n\tif (result != -1)\n\t\tstd::cout << "Element found at index " << result << std::endl;\n\telse\n\t\tstd::cout << "Element not found in the array." << std::endl;\n\treturn 0;\n}',

"Bubble Sort": '#include <iostream>\n\nvoid bubbleSort(int arr[], int n) {\n\tfor (int i = 0; i < n - 1; ++i) {\n\t\tfor (int j = 0; j < n - i - 1; ++j) {\n\t\t\tif (arr[j] > arr[j + 1]) {\n\t\t\t\tint temp = arr[j];\n\t\t\t\tarr[j] = arr[j + 1];\n\t\t\t\tarr[j + 1] = temp;\n\t\t\t}\n\t\t}\n\t}\n}\n\nint main() {\n\tint arr[] = {5, 2, 1, 3, 4};\n\tint n = sizeof(arr) / sizeof(arr[0]);\n\tbubbleSort(arr, n);\n\tstd::cout << "Sorted array: ";\n\tfor (int i = 0; i < n; ++i)\n\t\tstd::cout << arr[i] << " ";\n\tstd::cout << std::endl;\n\treturn 0;\n}'
}



def insert_program():

    selected_program = topic_combobox.get()

    if selected_program in cpp_programs:

        program_code = cpp_programs[selected_program]

        code_text.delete(1.0, tk.END)

        code_text.insert(tk.END, program_code)



# Tkinter GUI setup

root = tk.Tk()

root.title("C++ Program Generator Devloped By Mr.Sumit Gadwal")

root.geometry("600x400")



# Combobox to select program topics

topic_label = tk.Label(root, text="Select a C++ Program Topic:")

topic_label.pack(pady=(10, 5))

topic_combobox = ttk.Combobox(root, values=list(cpp_programs.keys()))

topic_combobox.pack(pady=5)



# Button to insert selected program

insert_button = tk.Button(root, text="Insert Program", command=insert_program)

insert_button.pack(pady=5)



# Text area to display program code

code_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)

code_text.pack(expand=True, fill="both")



# Label to display total number of programs

total_programs_label = tk.Label(root, text=f"Total Programs: {len(cpp_programs)}")

total_programs_label.pack(side="bottom", pady=5)



root.mainloop()

