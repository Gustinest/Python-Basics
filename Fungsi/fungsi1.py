import os

def clearscreen():
    os.system('CLS')

def echo(s):
    print(s)

def main():
    clearscreen()
    echo('Python 3')

if __name__ == '__main__':
    main()