import sys

def main():
    if len(sys.argv) < 3:
        sys.exit('Usage: %s input.in output.out'.format(sys.argv[0]))

    out = open(sys.argv[2], 'w')

    out.write('3\n')
    out.write('0 0 2 1\n')
    out.write('0 2 2 2\n')
    out.write('0 3 2 4\n')

if __name__ == '__main__':
    main()
