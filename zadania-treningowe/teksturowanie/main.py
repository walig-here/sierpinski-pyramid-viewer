from application import  Application
import sys


def main():
    if len(sys.argv) > 1:
        tetrix_levels = int(sys.argv[1])
        if tetrix_levels >= 2:
            app = Application("Tekstury", 800, 800)
            app.run(tetrix_levels)


if __name__ == '__main__':
    main()