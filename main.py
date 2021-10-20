

def read_list():
    given = input('Dați numerele separate prin virgulă: ')
    str_list = given.split(',')
    int_list = []
    for str_num in str_list:
        int_list.append(int(str_num))
    return int_list

def get_negatives(elem):
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

def print_menu():
    print('1. Citirea unei liste de numere intregi.')
    print('2. Afisarea tuturor numerelor negative nenule din lista.')
    print('3. Determinare cea mai lungă subsecvență de numere cu același număr de divizori.')
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
            print('Cea mai lungă subsecvență cu toate numerele prime este: ')
            print(result)
        elif option == '3':
            result = get_longest_sublist_all_equal_nr_of_divisors(lst)
            print('Cea mai lungă subsecvență formată doar din elemente cu același număr de divizori este: ')
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
    main()
