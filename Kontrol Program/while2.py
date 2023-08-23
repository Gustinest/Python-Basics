def main():
    total = 0 
    i = 1
    while i <= 5:
        print('%d' % i, end='')
        if i < 5:
            print(' + ', end='')
        else:
            print(' = ', end='')
        total += i
        i += 1

    print(total)
    
if __name__ == '__main__':
    main()
