

def read_list():
    given = input('Dați numerele separate prin virgulă: ')
    str_list = given.split(',')
    int_list = []
    for str_num in str_list:
        int_list.append(int(str_num))
    return int_list

def get_negatives(lst):
    '''
    Functia afiseaza numerele negative din lista.
    in: lista data de utilizator
    out: lista formata din numere negative
    '''
    result=[]
    for elem in lst:
        if elem < 0:
            result.append(elem)
        else:
            elem=elem+1
    return result

def test_get_negatives():
    assert get_negatives([-1,2,3,-14]) == [-1,-14]
    assert get_negatives([3,6,8,9]) ==[]
    assert get_negatives([])==[]

def get_smallest_number_same_last_digit(lst):
    '''
    Afiseaza cel mai mic nr cu aceeasi ultima cifra egala cu cifra data.
    in: lista data
    out: cel mai mic nr cu proprietatea data
    '''
    result=[]
    c=int(input('Dati cifra:'))
    for num in lst:
        if num%10==c:
            result.append(num)
        else:
            num=num+1
    return min(result)

def test_get_smallest_number():
    assert get_smallest_number_same_last_digit([12,2,34,15])==2
    assert get_smallest_number_same_last_digit([13,23,33])==13
    assert get_smallest_number_same_last_digit([16,76,8,5])==16

def print_menu():
    print('1. Citirea unei liste de numere intregi.')
    print('2. Afisarea tuturor numerelor negative nenule din lista.')
    print('3. Afisarea celui mai mic numar cu ultima cifra egala cu o cifra data.')
    print('4. Determinare cea mai lungă subsecvență de palindroame.')
    print('x. Ieșire.')


def main():
    lst = []
    while True:
        print_menu()
        option = input('Alegeți opțiunea: ')
        if option == '1':
            lst = read_list()
        elif option == '2':
            result = get_negatives(lst)
            print('Lista cu toate numerele negative nenule: ')
            print(result)
        elif option == '3':
            result = get_smallest_number_same_last_digit(lst)
            print('Cel mai mic nr cu ultima cifra egala cu cifra data este: ')
            print(result)
        elif option == '4':
            result = get_longest_sublist_all_palindrome(lst)
            print('Cea mai lungă subsecvență cu palindroame este: ')
            print(result)
        elif option == 'x':
            break
        else:
            print('Opțiune invalidă, reîncearcă!')

if __name__ == '__main__':
    test_get_negatives()
    main()
