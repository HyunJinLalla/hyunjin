def rev_str(input_str): #재귀함수 프로그램
    reversed_str = ''
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str

if __name__ == '__main__':
    print(rev_str('ABCDE'))
    print(rev_str('Come again, Forever young!'))
    print(rev_str('Amore, Roma'))