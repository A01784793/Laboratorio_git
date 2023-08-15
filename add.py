import math
import sys

def degrees_to_radians(degrees):
    return degrees * math.pi / 180

def radians_to_degrees(radians):
    return radians * 180 / math.pi

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: degrees.py <convert-from> <value>')
        print('  convert-from: "degrees" or "radians"')
        print('  value: the value to convert')
        sys.exit(1)

    convert_from = sys.argv[1]
    value = float(sys.argv[2])

    if convert_from == 'degrees':
        print(f'{value} degrees is {degrees_to_radians(value):.4f} radians')
    elif convert_from == 'radians':
        print(f'{value} radians is {radians_to_degrees(value):.4f} degrees')
    else:
        print(f'Invalid convert-from value: {convert_from}')
        sys.exit(1)
