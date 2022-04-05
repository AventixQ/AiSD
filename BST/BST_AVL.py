import sys
from random import randint


class BST:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None


class AVL:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None
        self.height = 1


def insert_AVL(root, key):
    if not root:
        return AVL(key)
    elif key < root.key:
        root.left_child = insert_AVL(root.left_child, key)
    else:
        root.right_child = insert_AVL(root.right_child, key)
    root.height = 1 + max(heightGet(root.left_child), heightGet(root.right_child))
    # balance factor
    balancing = balance(root)
    if balancing > 1 and key < root.left_child.key:  # ll
        return rightR(root)
    if balancing < -1 and key > root.right_child.key:  # rr
        return leftR(root)
    if balancing > 1 and key > root.left_child.key:  # lr
        root.left_child = leftR(root.left_child)
        return rightR(root)
    if balancing < -1 and key < root.right_child.key:  # rl
        root.right_child = rightR(root.right_child)
        return leftR(root)
    return root


def leftR(l):  # left Rotate
    a = l.right_child
    b = a.left_child
    a.left_child = l
    l.right_child = b

    l.height = 1 + max(heightGet(l.left_child), heightGet(l.right_child))
    a.height = 1 + max(heightGet(a.left_child), heightGet(a.right_child))

    return a  # new root


def rightR(l):  # right rotate
    a = l.left_child
    b = a.right_child
    a.right_child = l
    l.left_child = b

    l.height = 1 + max(heightGet(l.left_child), heightGet(l.right_child))
    a.height = 1 + max(heightGet(a.left_child), heightGet(a.right_child))

    return a  # new root


def heightGet(root):
    if not root:
        return 0
    return root.height


def balance(root):  # for AVL
    if not root:
        return 0
    a = heightGet(root.left_child) - heightGet(root.right_child)
    return a


def storeBTS(root, tab):
    if root is None:
        return
    storeBTS(root.left_child, tab)
    tab.append(root)
    storeBTS(root.right_child, tab)


def construct(tab, s, e):
    if s > e:
        return None
    center = int((s + e) / 2)
    node = tab[center]
    node.left_child = construct(tab, s, center - 1)
    node.right_child = construct(tab, center + 1, e)
    return node


def balanced(root):  # for BST
    tab = []
    storeBTS(root, tab)
    n = len(tab)
    x = construct(tab, 0, n - 1)
    return x


def insert_BST(bst, key):
    if bst is None:
        return BST(key)

    if key < bst.key:
        bst.left_child = insert_BST(bst.left_child, key)
    else:
        bst.right_child = insert_BST(bst.right_child, key)

    return bst


def in_order(root):
    if root is not None:
        in_order(root.left_child)
        print(root.key, end=" ")
        in_order(root.right_child)


def pre_order(root):
    if root is not None:
        print(root.key, end=" ")
        pre_order(root.left_child)
        pre_order(root.right_child)


def post_order(root, tab):
    if root is None:
        return
    post_order(root.left_child, tab)
    post_order(root.right_child, tab)
    tab.append(root.key)


def find_min(root):
    if root is None:
        print("Drzewo jest puste!")
        return
    temp = root
    while temp.left_child is not None:
        print(temp.key, end="->")
        temp = temp.left_child
    print(temp.key)
    return temp.key


def find_max(root):
    if root is None:
        print("Drzewo jest puste!")
        return
    temp = root
    while temp.right_child is not None:
        print(temp.key, end="->")
        temp = temp.right_child
    print(temp.key)
    return temp.key


def find_and_print(root, key):
    if root is None:
        print("Drzewo jest puste!")
        return
    if key == root.key:
        return pre_order(root)

    if key < root.key:
        return find_and_print(root.left_child, key)

    return find_and_print(root.right_child, key)


def delete_BST(root, value):
    if not root:
        return root
    if value < root.key:
        root.left_child = delete_BST(root.left_child, value)
    elif value > root.key:
        root.right_child = delete_BST(root.right_child, value)
    else:
        if root.left_child is None:
            temp = root.right_child
            root = None
            return temp
        elif root.right_child is None:
            temp = root.left_child
            root = None
            return temp
        temp = min_val(root.right_child)
        root.key = temp.key
        root.right_child = delete_BST(root.right_child, temp.key)
    if root is None:
        return root


def delete_AVL(root, key):
    if not root:
        return root
    elif key < root.key:
        root.left_child = delete_AVL(root.left_child, key)
    elif key > root.key:
        root.right_child = delete_AVL(root.right_child, key)
    else:
        if root.left_child is None:
            a = root.right_child
            root = None
            return a
        if root.right_child is None:
            a = root.left_child
            root = None
            return a
        a = min_val(root.right_child)
        root.key = a.key
        root.right_child = delete_AVL(root.right_child, a.key)
    if root is None:
        return root

    root.height = 1 + max(heightGet(root.left_child), heightGet(root.right_child))

    balancing = balance(root)  # balancing tree
    if balancing > 1 and key < root.left_child.key:  # ll
        return rightR(root)
    if balancing < -1 and key > root.right_child.key:  # rr
        return leftR(root)
    if balancing > 1 and key > root.left_child.key:  # lr
        root.left_child = leftR(root.left_child)
        return rightR(root)
    if balancing < -1 and key < root.right_child.key:  # rl
        root.right_child = rightR(root.right_child)
        return leftR(root)
    return root


def min_val(root):
    if root is None or root.left_child is None:
        return root
    return min_val(root.left_child)


def random_number_generator(n):
    tab = []
    for x in range(n):
        tab.append(randint(10, 10 * n))
    return tab


def insertion_binary(tab):
    if not tab:
        return
    median = len(tab) // 2
    root = AVL(tab[median])
    root.right_child = insertion_binary(tab[:median])
    root.left_child = insertion_binary(tab[median + 1:])
    return root


def heap(t, n, i):
    maxi = i
    childleft = 2 * i + 1
    childright = 2 * i + 2
    if childleft < n and t[childleft] < t[i]:
        maxi = childleft
    if childright < n and t[childright] < t[maxi]:
        maxi = childright
    if maxi != i:
        t[i], t[maxi] = t[maxi], t[i]
        heap(t, n, maxi)


def heapsort(t, n):
    for x in range(n//2, -1, -1):
        heap(t, n, x)
    for y in range(n-1, 0, -1):
        t[y], t[0] = t[0], t[y]
        heap(t, y, 0)


post_order_tab = []
while True:
    root = None
    print("Menu:\n1 - Dane wejściowe\n2 - Testy\n3 - Zakończ działanie programu")
    x = input()
    if x == "1":
        print("Wybierz rodzaj drzewa (BST/AVL): ")
        choose = input()
        if choose != 'BST' and choose != "AVL":
            print("To chyba nie jest poprawna wartosc! Sprobuj ponownie.")
            continue
        print("Ile chcesz podać liczb?")
        ile_liczb = input()
        if ile_liczb.isnumeric():
            ile_liczb = int(ile_liczb)
            ile = 0
            dane = []
            while ile < ile_liczb:
                number = input()
                if number.isnumeric():
                    dane.append(int(number))
                    ile += 1
                else:
                    print("To nie jest liczba! Spróbuj ponownie")
            if choose == 'BST':
                for x in dane:
                    root = insert_BST(root, x)
            else:
                heapsort(dane, len(dane))
                for y in dane:
                    root = insert_AVL(root, y)
            while True:
                print("Menu procedur:\n1 - Wyszukiwanie min i max\n2 - Usunięcie elementu\n3 - Wypisanie in-order"
                      "\n4 - Wypisanie pre-order\n5 - Usunięcie całego drzewa(post-order)\n6 - Wypisanie pre-order podrzewa"
                      "\n7 - Równoważenie drzewa\n8 - Powrót do menu głównego")
                chosen = int(input())
                if type(chosen) == int:
                    if chosen == 1:
                        print("Największa wartość : ")
                        find_max(root)
                        print("Najmniejsza wartość : ")
                        find_min(root)
                        print("\n")
                    if chosen == 2:
                        print("Podaj ile wartości chcesz usunąć: ")
                        value = int(input())
                        if type(value) == int:
                            for v in range(value):
                                value_td = int(input())  # Błąd
                                if type(value_td) == int:
                                    if choose == 'BST':
                                        root = delete_BST(root, value_td)  # Błąd
                                    else:
                                        root = delete_AVL(root, value_td)
                        print("\n")
                    if chosen == 3:
                        print("In-order")
                        in_order(root)
                        print("\n")
                    if chosen == 4:
                        print("Pre-order")
                        pre_order(root)
                        print("\n")
                    if chosen == 5:
                        print("Delete post-order")
                        if choose == 'BST':
                            post_order(root, post_order_tab)
                            for x in post_order_tab:
                                root = delete_BST(root, x)
                        else:
                            post_order(root, post_order_tab) # sprawdzić / czasem działa
                            for x in post_order_tab:
                                root = delete_AVL(root, x)
                        print("\n")
                    if chosen == 6:
                        print("Podaj klucz do podrzewa: ")
                        key = input()   # Błąd
                        if key.isnumeric():
                            print("Find a key")
                            find_and_print(root, int(key))
                            print("\n")
                        else:
                            print("To nie jest poprawna wartość!")
                    if chosen == 7:
                        if choose == 'BST':
                            pre_order(balanced(root))
                            print("\n")
                        else:
                            print("To drzewo jest już zrównoważone!")
                    if chosen == 8:
                        break
        else:
            print("To nie jest liczba podaj poprawną wartość!")
    elif x == "2":
        print(x)
    elif x == "3":
        sys.exit()
    else:
        print("Podaj poprawną wartość")
