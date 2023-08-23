import os
def main():
    # emebuka file
    f = open('data1.txt', 'r')

    # membaca data
    data = f.read()

    #menampilkan data
    print(data)

    
    # Menutup file
    f.close()

if __name__ == '__main__':
    main()