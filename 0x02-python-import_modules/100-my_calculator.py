#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys
    length = len(sys.argv) - 1

    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    result = 0

    if op == "+":
        result = calc.add(a, b)
    elif op == "-":
        result = calc.sub(a, b)
    elif op == "*":
        result = calc.mul(a, b)
    elif op == "/":
        result = calc.div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{:d} {} {:d} = {:d}".format(a, op, b, result))
    sys.exit(0)
