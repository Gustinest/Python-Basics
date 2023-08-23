def echo(value, newline=True):
    if newline:
        print(value)
    else:
        print(value, end=" ")

echo('kamu')
echo('kita', False)
echo('aku', True)

if __name__ == '__echo__':
    echo()

    