def kali(a, b):
    return a * b

def echo(s, n):
    for i in range (n):
        print(s)

def main():
    print('Pemanggilan fungsi pertama kali(): ')
    print(" 2 * 3 = %d " % kali(2, 3)) # Parameter
    print('\n')
    print('Pemanggilan kedua fungsi kali(): ')
    print(" 10 * 20 = %d " % kali(10, 20))
    
    print('\n\n')

    print('Pemanggilan pertama fungsi echo()')
    echo('python', 5) # Parameter
    print("\n")
    print('Pemanggilan kedua fungsi echo()')
    echo('pemrograman python', 3)

if __name__ == '__main__':
    main()


