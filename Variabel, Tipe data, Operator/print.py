def  main():
    bahasa = 'python'
    versi = 3

    print(bahasa, versi)
    print(bahasa + ' ' + str(versi))
    print('%s %d' % (bahasa, versi))
    print('{} {}'. format(bahasa, versi))
    print('{0} {1}'.format(bahasa, versi))

if __name__ == "__main__":
    main()